"""
The file contains an adjacency list representation of an undirected weighted graph with 200 vertices labeled 1 to 200. 
Each row consists of the node tuples that are adjacent to that particular vertex along with the length of that edge. 
For example, the 6th row has 6 as the first entry indicating that this row corresponds to the vertex labeled 6. The 
next entry of this row "141,8200" indicates that there is an edge between vertex 6 and vertex 141 that has length 8200. 
The rest of the pairs of this row indicate the other vertices adjacent to vertex 6 and the lengths of the corresponding 
edges.

Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1 (the first vertex) as the source vertex, 
and to compute the shortest-path distances between 1 and every other vertex of the graph. If there is no path between a 
vertex  and vertex 1, we'll define the shortest-path distance between 1 and  to be 1000000.

You should report the shortest-path distances to the following ten vertices, in order: 7,37,59,82,99,115,133,165,188,197. 
You should encode the distances as a comma-separated string of integers. So if you find that all ten of these vertices 
except 115 are at distance 1000 away from vertex 1 and 115 is 2000 distance away, then your answer should be 
1000,1000,1000,1000,1000,2000,1000,1000,1000,1000. Remember the order of reporting DOES MATTER, and the string should be 
in the same order in which the above ten vertices are given. The string should not contain any spaces. Please type your 
answer in the space provided.

"""

import re
from heapq import heapify, heappush, heappop

class Solution(object):
	
	def __init__(self, fname):

		self.G = {}  # it is an undirected graph, so in-edges are the same as out-edges

		with open(fname, 'r') as f:
			for line in f.readlines():
				line_list = re.split('\t| ', line.strip())
				V = int(line_list[0])

				E = {int(n): int(w) for n, w in zip([x.split(',')[0] for x in line_list[1:]],
											  [x.split(',')[1] for x in line_list[1:]])}

				self.G[V] = E



	def dijkstra(self, start):

		# this is the `vanilla' version with O(mn) time

		self.X = set()  # set of included nodes
		self.dist = {}  # distance from start vertex

		# init the dist ditc
		for n in self.G:
			self.dist[n] = float('inf')
		
		self.dist[start] = 0
		self.X.add(start)

		# start the main loop
		while len(self.X) < len(self.G):
			# print('X: ', self.X)
			candidates = {}
			for n in self.X:  # visit each node in the set X
				for child in self.G[n]:  # test its outgoing edges:
					if child not in self.X:  # the node is not included
						# update the dijkstra's greedy score
						self.dist[child] = min(self.dist[child], self.dist[n] + self.G[n][child])
						candidates[child] = min(self.dist[child], candidates.get(child, float('inf')))

			# now I have to decide which vertex to include
			tmp_min = float('inf')
			# print('candidates: ', candidates)
			for x in candidates:
				if candidates[x] < tmp_min:
					tmp_min = candidates[x]
					next_v = x
			self.X.add(next_v)

	def dijkstra_heap(self, start):

		# this is the implementation with heap, to get O(mlogn) time
		# modified from here: https://gist.github.com/kachayev/5990802

		self.Q = [(0, start, [])]  # this is the unvisited heap
		self.visited = set()  # this is the visited nodes
		self.dist = {}  # collect distances

		while self.Q:  # as long as there are still unvisited nodes
			(cost, node, path) = heappop(self.Q)
			if node not in self.visited:
				self.dist[node] = cost

			if node not in self.visited:
				self.visited.add(node)  # put it in the visited list
				path.append(node)

				for child in self.G[node]:
					if child not in self.visited:
						heappush(self.Q, (self.G[node][child] + cost, child, path))





if __name__ == '__main__':
	fname = 'hw2.txt'
	S = Solution(fname)

	def get_answer(S):
		nodes = [7,37,59,82,99,115,133,165,188,197]
		answers = []
		for n in nodes:
			answers.append(S.dist[n])
		print(answers)
	
	S.dijkstra(1)
	get_answer(S)
	
	S.dijkstra_heap(1)
	get_answer(S)
	



