#!/usr/bin/env python3

"""
This file describes a distance function (equivalently, a complete graph with edge costs). 
It has the following format:

[number_of_nodes]

[edge 1 node 1] [edge 1 node 2] [edge 1 cost]

[edge 2 node 1] [edge 2 node 2] [edge 2 cost]

...


There is one edge (i,j) for each choice of 1≤i<j≤n, where n is the number of nodes.

For example, the third line of the file is "1 3 5250", indicating that the distance between 
nodes 1 and 3 (equivalently, the cost of the edge (1,3)) is 5250. You can assume that distances 
are positive, but you should NOT assume that they are distinct.

Your task in this problem is to run the clustering algorithm from lecture on this data set, 
where the target number k of clusters is set to 4. What is the maximum spacing of a 4-clustering?
"""
from UnionFind import UnionFind

class Solution:

	def __init__(self, fname):

		self.E = []  # edges
		self.V = set()

		with open(fname, 'r') as f:
			self.N = f.readline()
			for line in f.readlines():
				n1, n2, d = list(map(int, line.split()))
				self.E.append((d, n1, n2))
				self.V.add(n1)
				self.V.add(n2)

		self.E.sort(reverse=True)  # descending order
		print(self.E[0])

	def clustering(self, k):
		n_clusters = len(self.V)
		
		# init the Union find
		self.X = UnionFind()
		for v in self.V:
			self.X[v]  
		
		while n_clusters > k:
			e, n1, n2 = self.E.pop()
			if self.X[n1] != self.X[n2]:  # only union if the two nodes are not in the same cluster
				self.X.union(n1, n2)
				n_clusters -= 1

		# now let's find out the *minimum* spacing for any pair of nodes that are in different clusters
		res = float('inf')
		while self.E:
			e, n1, n2 = self.E.pop()
			if self.X[n1] != self.X[n2]:
				res = min(e, res)

		print(res)


if __name__ == '__main__':

	fname = 'hw2_1.txt'
	S = Solution(fname)
	S.clustering(4)
