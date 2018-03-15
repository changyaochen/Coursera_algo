#!/usr/bin/env python3

"""
In this programming problem you'll code up the dynamic programming algorithm for computing a maximum-weight 
independent set of a path graph.

Download the text file below.

mwis.txt
This file describes the weights of the vertices in a path graph (with the weights listed in the order in 
which vertices appear in the path). It has the following format:

[number_of_vertices]

[weight of first vertex]

[weight of second vertex]

...

For example, the third line of the file is "6395702," indicating that the weight of the second vertex of 
the graph is 6395702.

Your task in this problem is to run the dynamic programming algorithm (and the reconstruction procedure) 
from lecture on this data set. The question is: of the vertices 1, 2, 3, 4, 17, 117, 517, and 997, which 
ones belong to the maximum-weight independent set? (By "vertex 1" we mean the first vertex of the 
graph---there is no vertex 0.) In the box below, enter a 8-bit string, where the ith bit should be 1 
if the ith of these 8 vertices is in the maximum-weight independent set, and 0 otherwise. For example, 
if you think that the vertices 1, 4, 17, and 517 are in the maximum-weight independent set and the other 
four vertices are not, then you should enter the string 10011010 in the box below.
"""

from heapq import heapify, heappush, heappop

class Solution:

	def __init__(self, fname):
		
		self.L = []
		with open(fname, 'r') as f:
			self.N = int(f.readline())
			for x in f.readlines():
				self.L.append(int(x))


	def run(self):
		dp = [-1]*len(self.L)
		dp[0] = self.L[0]
		dp[1] = max(self.L[:2])
		
		for i in range(2, len(self.L)):
			dp[i] = max(dp[i-1], dp[i-2] + self.L[i])

		self.dp = dp.copy()

		ind = {}
		i = self.N-1
		
		while i >= 0:			
			if dp[i] == dp[i-1]:
				i -= 1
			else:
				ind[i+1] = 1
				i -= 2


		res = []
		for x in [1, 2, 3, 4, 17, 117, 517, 997]:
			if x in ind:
				res.append('1')
			else:
				res.append('0')

		print(''.join(res))

		
		return ind


if __name__ == '__main__':
	fname = 'hw3_3.txt'
	S = Solution(fname)
	ind = S.run()
	




	