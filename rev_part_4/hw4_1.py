#!/usr/bin/env python3

"""
In this assignment you will implement one or more algorithms for the all-pairs shortest-path problem. 
Here are data files describing three graphs:

g1.txt
g2.txt
g3.txt

The first line indicates the number of vertices and edges, respectively. Each subsequent line describes 
an edge (the first two numbers are its tail and head, respectively) and its length (the third number). 
NOTE: some of the edge lengths are negative. NOTE: These graphs may or may not have negative-cost cycles.

Your task is to compute the "shortest shortest path". Precisely, you must first identify which, if any, 
of the three graphs have no negative cycles. For each such graph, you should compute all-pairs shortest 
paths and remember the smallest one (i.e., compute minu,v∈Vd(u,v), where d(u,v) denotes the shortest-path 
	distance from u to v).

If each of the three graphs has a negative-cost cycle, then enter "NULL" in the box below. If exactly one 
graph has no negative-cost cycles, then enter the length of its shortest shortest path in the box below. 
If two or more of the graphs have no negative-cost cycles, then enter the smallest of the lengths of their 
shortest shortest paths in the box below.
"""
import copy, time

class Solution:

	def __init__(self, fname):
		
		self.G = {} # The format of G should be in the dictionary form of 
		            # {tail_1: [(head_1, weight_1), head_2, weight_2), head_3, weight_3), ...], tail_2: [...], ....}
					# we also use 1-base index for vertices
		
		with open(fname, 'r') as f:
			self.n, self.m = list(map(int, f.readline().split()))
			for line in f.readlines():
				tail, head, weight = list(map(int, line.split()))
				if tail not in self.G:
					self.G[tail] = [(head, weight)]
				else:
					self.G[tail].append((head, weight))

		# one more pass to fill possible vertex with no out-edge
		for i in range(1, self.n+1):
			if i not in self.G:
				self.G[i] = []

	def Bellman_Ford(self, s, G):
		"""
		implementation of Bellman-Ford algorithm to find shorted path between 
		vertex s and all vertices, given the graph G. 

		The format of G should be in the dictionary form of 
		{tail_1: [(head_1, weight_1), head_2, weight_2), head_3, weight_3), ...], tail_2: [...], ....}
		"""
		
		# dp array, the shortest path from t to each vertex
		n = len(G.keys())
		dp = {v: float('inf') for v in range(1, n+1)}
		dp[s] = 0  # init step

		# main loop, run for n-1 time
		print('Running Bellman-Ford algorithm...')
		for i in range(n-1):
			print('Step {} of {}...'.format(i, n), end='\r')
			dp_last = dp.copy()
			# inner for-loop, looping through all vertices
			# I will 'push' the new values to the head vertex
			for v in G.keys():
				for h, w in G[v]:
					dp[h] = min(dp[h], dp[v] + w)

			# check for early stop
			if dp == dp_last:
				print('\nEarly termination of Bellman-Ford.')
				return dp
			else:
				dp_last = dp.copy()

		# check for negative cost cycle
		for v in G.keys():
			for h, w in G[v]:
				dp[h] = min(dp[h], dp[v] + w)
		if dp != dp_last:
			print('\nThere is a negative cost cycle. Exit the algorithm.')
			return None

		return dp

	def APSP_1(self):
		""" 
		vanilla implemenation of all-pair shortest path
		looping through all vertex, inovke Bellman-Ford at each vertex
		"""

		res = float('inf')
		for s in self.G.keys():
			print('Working on node {} of total {} nodes.'.format(s, self.n), end='\r')
			dp = self.Bellman_Ford(s, self.G)
			res = min(res, min(dp.values()))

		return res

	def APSP_2(self):
		# Floyd-Warshall algorithm

		# n x n array, 0-based
		A = [[float('inf') for _ in range(self.n)] for _ in range(self.n)]
		
		# first pass
		for i in self.G:  # v is 1-based index
			A[i-1][i-1] = 0
			for (j, c) in self.G[i]:
				A[i-1][j-1] = c
		A_last = copy.deepcopy(A)

		# main loop, looping through k
		t_start = time.time()
		for k in range(100):
			print('Running step {} of total {}... time elapsed {:6.2f} minutes.'\
				.format(k, self.n, (time.time() - t_start)/60), end='\r')
			for i in range(self.n):
				for j in range(self.n):
					A[i][j] = min(A_last[i][j], A_last[i][k] + A_last[k][j])

			A_last = copy.deepcopy(A)

		# check for negative cost cycle, also check for result
		res = float('inf')
		for i in range(self.n):
			res = min(A[i])
			if A[i][i] < 0:
				print('\nThere is a negative cost cycle.')
				return None
		
		return res


	def APSP_3(self):
		# TODO: Johnson's algorithm
		pass



if __name__ == '__main__':
	# fname = 'Bellman_Ford_debug.txt'
	fname = 'g3.txt'
	S = Solution(fname)
	res = S.APSP_2()






