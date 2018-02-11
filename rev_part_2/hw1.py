#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 22:40:57 2018

The file contains the edges of a directed graph. Vertices are labeled as 
positive integers from 1 to 875714. Every row indicates an edge, the vertex
 label in first column is the tail and the vertex label in second column is
 the head (recall the graph is directed, and the edges are directed from 
 the first column vertex to the second column vertex). So for example, the 
 row looks liks : "2 47646". This just means that the vertex with label 2 
 has an outgoing edge to the vertex with label 47646

Your task is to code up the algorithm from the video lectures for computing
 strongly connected components (SCCs), and to run this algorithm on the 
 given graph.

@author: changyaochen
"""

from sys import setrecursionlimit
setrecursionlimit(4000000)
import re

class Solution(object):
	
	def __init__(self, fname):
		
		self.G = {}
		self.G_rev = {}
		self.visited_1 = set()  # 'visited' nodes for first dfs
		self.visited_2 = set()  # 'visited' nodes for second dfs
		self.stack_1 = []  # stack for the first dfs
		self.stack_2 = []  # stack for the second dfs
		self.scc = {}  # scc dict
		self.tmp_group = []
		self.i = 0
		
		
		with open(fname, 'r') as f:
			for line in f.readlines():
				k, v = re.split(',| ', line)
				k, v = int(k), int(v)
				if k not in self.G:
					if k != v:  # make no self loop
						self.G[k] = [v]
					else:
						continue
				else:
					self.G[k].append(v)
				
				# make the reverse graph
				if v not in self.G_rev:
					if k != v:  # make no self loop
						self.G_rev[v] = [k]
					else: 
						continue
				else:
					self.G_rev[v].append(k)
		self.all_nodes = list(set(self.G.keys()) 
							| set(self.G_rev.keys()))
		self.L = []  # finishing order list
		self.all_nodes.reverse()

		
		# pad both graphs for nodes with no outgoing arcs
		for node in self.all_nodes:
			if node not in self.G:
				self.G[node] = []
			if node not in self.G_rev:
				self.G_rev[node] = []
		
		return 
	
	def dfs_1(self, start):
		# iterative call for dfs
		tmp = []  # finishing order in this dfs
		self.stack_1.append(start)
		while len(self.stack_1) > 0:
			node = self.stack_1.pop()
			if node not in self.visited_1:
				self.visited_1.add(node)  # add to the visited set
				tmp.append(node)
				
				# push all its un-visited child nodes to the stack
				for child in self.G_rev[node]:
					if child not in self.visited_1:
						self.stack_1.append(child)
		tmp.reverse()

		return tmp

		
	def dfs_2(self, start, i_or_r='i'):

		if i_or_r == 'i':
			# iterative call
			self.stack_2.append(start)
			self.scc[self.i].add(start)
			
			while self.stack_2:
				node = self.stack_2.pop()
				if node not in self.visited_2:
					self.visited_2.add(node)

					# push the un-visited nodes to the stack
					for child in self.G[node]:
						if child not in self.visited_2:
							self.stack_2.append(child)
							# also add this node to the running scc
							self.scc[self.i].add(child)

		elif i_or_r == 'r':
			# recursive call
			# base case
			if start in self.visited_2:
				return
			
			# print('going out from: ', node)
			self.visited_2.add(start)
			self.scc[self.i].add(start)
			
			for child in self.G[start]:
				self.dfs_2(child)
			
			return start  # only return a node when it is not 'back-tracked'

		else:
			raise Exception('Unknow choice.')
			 
		
	
	def run(self):
		# first DFS call, to get the finishing order
		for node in self.all_nodes:
			if node not in self.visited_1:
				# print('going out from: ', node)
				tmp = self.dfs_1(node)
				self.L.extend(tmp)
		# print(self.L)
		print('Done with first dfs!')
		
		# second DFS call
		while len(self.L) > 0:
			start = self.L.pop()  # going from last finished nodes
			if start not in self.visited_2:
				self.i += 1
				self.scc[self.i] = set()
				self.dfs_2(start, i_or_r='i')
		print('Done with second dfs!')

		# get scc size
		self.sizes = list(map(len, self.scc.values()))
		self.sizes.sort(reverse=True)
		print('top 5 scc: ', self.sizes[:5])
				
		


if __name__ == '__main__':
	fname = 'hw1_debug_2738_240_140_42_36.txt'
	fname = 'hw1.txt'
	S = Solution(fname)
	S.run()
	# print(S.scc)
	