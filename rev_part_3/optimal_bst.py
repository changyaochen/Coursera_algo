#!/usr/bin/env python3

"""
Here we are going to calculate the weight search time for the optimal BST

In the file with n rows, we infer the row number as the search key,
and the value of that row as the frequency (a value between 0.0 and 1.0)

The output will be the search time of the optimal BST

With input of 
0.05
0.4
0.08
0.04
0.1
0.1
0.23

The correct answer is 2.18
"""

import numpy as np

class Solution:

	def __init__(self, fname):

		self.keys = []
		self.freqs = []
		with open(fname, 'r') as f:
			for i, line in enumerate(f.readlines()):
				self.keys.append(i)
				self.freqs.append(float(line))
		self.n = len(self.keys)

	def run(self):
		
		# this is the main loop for the dp

		A = [[0 for _ in range(self.n)] for _ in range(self.n)]

		for s in range(self.n):
			for i in range(self.n):
				all_candidates = []
				for r in range(i, i+s+1):
					
					if r >= self.n:
						continue
					
					if i <= r-1:
						left = A[i][r-1]
					else:
						left = 0

					if r+1 <= i+s and i+s < self.n:
						right = A[r+1][i+s]
					else:
						right = 0
					all_candidates.append(left + right)
				
				if i+s < self.n:
					A[i][i+s] = min(all_candidates) + sum(self.freqs[i:i+s+1])

		return A[0][-1]


if __name__ == '__main__':
	fname = 'optimal_bst.txt'
	S = Solution(fname)
	res = S.run()  




	