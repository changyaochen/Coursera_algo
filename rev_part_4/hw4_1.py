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

class Solution:

	def __init__(self, fname):
		self.G = {}

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

	def run(self):

		return self.Bellman_Ford(1, self.G)



if __name__ == '__main__':
	fname = 'Bellman_Ford_debug.txt'
	fname = 'g3.txt'
	S = Solution(fname)
	dp = S.run()






