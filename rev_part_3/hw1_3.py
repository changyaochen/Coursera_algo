#!/usr/bin/env python3
"""
This file describes an undirected graph with integer edge costs. It has the format

[number_of_nodes] [number_of_edges]

[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]

[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]

...

For example, the third line of the file is "2 3 -8874", indicating that there is an edge connecting vertex 
#2 and vertex #3 that has cost -8874.

You should NOT assume that edge costs are positive, nor should you assume that they are distinct.

Your task is to run Prim's minimum spanning tree algorithm on this graph. You should report the overall cost 
of a minimum spanning tree --- an integer, which may or may not be negative --- in the box below.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Prim's 
algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing a 
heap-based version. The simpler approach, which should already give you a healthy speed-up, is to maintain 
relevant edges in a heap (with keys = edge costs). The superior approach stores the unprocessed vertices in 
the heap, as described in lecture. Note this requires a heap that supports deletions, and you'll probably need 
to maintain some kind of mapping between vertices and their positions in the heap.
"""

from heapq import heappush, heappop
import time

class Solution(object):
	
	def __init__(self, fname):
		self.G_1 = {}
		self.G_2 = {}  # this is for the heap implementation
		self.E = []  # this will be a heap, with cost as the key
		with open(fname, 'r') as f:
			self.n, self.m = f.readline().split()
			for line in f.readlines():
				n1, n2, cost = list(map(int, line.split()))
				# process n1
				if n1 not in self.G_1:
					self.G_1[n1] = [(n2, cost)]
				else:
					self.G_1[n1].append((n2, cost))
				# process n2
				if n2 not in self.G_1:
					self.G_1[n2] = [(n1, cost)]
				else:
					self.G_1[n2].append((n1, cost))

				# ===== below if for the heap implementation
				if n1 not in self.G_2:
					self.G_2[n1] = [(cost, n2)]
				else:
					heappush(self.G_2[n1], (cost, n2))

				if n2 not in self.G_2:
					self.G_2[n2] = [(cost, n1)]
				else:
					heappush(self.G_2[n2], (cost, n1))

				# to store edges as heap
				heappush(self.E, (cost, n1, n2))


	def run1(self):
		# vanilla implementation of Prim's algorithm with O(mn) time
		visited = set()
		MST_cost = 0

		# visit a random first node
		start = list(self.G_1.keys())[0]
		visited.add(start)

		
		# main loop
		while len(visited) < len(self.G_1):
			tmp_min = float('inf')
			candidate = -1

			# find next node to absorbe
			for node in visited:
				for end, cost in self.G_1[node]:
					if end not in visited: 
						if cost < tmp_min:
							tmp_min, candidate = cost, end

			visited.add(candidate)
			MST_cost += tmp_min

		return MST_cost

	def check_crossing(self, n1, n2, S1, S2):
		# return True is the edge (n1, n2) crosses the cut (S1, S2)
		if ((n1 in S1) and (n2 in S2)) or ((n1 in S2) and (n2 in S1)):
			return True
		else:
			return False

	def check_one_set(self, n1, n2, S):
		# return True if the edge (n1, n2) lies in the set S
		if (n1 in S) and (n2 in S):
			return True
		else:
			return False

	def run2(self):
		# fast implementation 1 with heap
		visited = set()
		unvisited = set(self.G_2.keys())
		MST_cost = 0

		# visit a random first node
		start = list(self.G_1.keys())[0]
		visited.add(start)
		unvisited.remove(start)

		# main loop
		while len(unvisited) > 0:
			# print('visited ', visited)
			# print('unvisited ', unvisited)
			tmp_list = []
			cost, n1, n2 = heappop(self.E)
			while not self.check_crossing(n1, n2, visited, unvisited) and len(self.E) > 0:  # not a crossing edge
				if self.check_one_set(n1, n2, unvisited):
					tmp_list.append((cost, n1, n2))  # we will push this back to the heap later
				cost, n1, n2 = heappop(self.E)
			
			# we will only exit if we have found a crossing edge
			# print(n1, n2)
			MST_cost += cost
			if n1 in visited:
				visited.add(n2)
				unvisited.remove(n2)
			else:
				visited.add(n1)
				unvisited.remove(n1)
			
			# we will push the edges lie in unvisited set back into the heap
			for x in tmp_list:
				heappush(self.E, x)

		return MST_cost





if __name__ == '__main__':
	fname = 'hw1_3.txt'
	S = Solution(fname)
	t1 = time.time()
	print('MST cost with run 1 is: {}'.format(S.run1()))
	print('Time of run 1 is: {:3.6f} seconds'.format(time.time() - t1))

	t2 = time.time()
	print('\nMST cost with run 2 is: {}'.format(S.run2()))
	print('Time of run 2 is: {:3.6f} seconds'.format(time.time() - t2))

