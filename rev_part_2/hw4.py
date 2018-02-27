#!/usr/bin/env python3

"""
The goal of this problem is to implement a variant of the 2-SUM algorithm covered in this week's 
lectures.

The file contains 1 million integers, both positive and negative (there might be some repetitions!).
This is your array of integers, with the ith row of the file specifying the ith entry of the array.

Your task is to compute the number of target values t in the interval [-10000,10000] (inclusive) 
such that there are distinct numbers x,y in the input file that satisfy x+y=t. (NOTE: ensuring 
distinctness requires a one-line addition to the algorithm from lecture.)
"""

class Solution(object):

	def __init__(self, fname):

		self.L = []
		with open(fname, 'r') as f:
			for line in f.readlines():
				self.L.append(int(line))
		# remove duplicate
		self.L = list(set(self.L))
		self.L.sort()
		self.N = len(self.L) - 1

	def binary_search(self, L, target, low, high):
		# L is a sorted list in ascending order
		# if not found, we will return the idx of the target to the target's right
		if low >= high:
			return high
		if target == L[low]:
			return low
		if target == L[high]:
			return high
				
		mid = low + (high - low) // 2
		if target > L[mid]:
			res = self.binary_search(L, target, mid+1, high)
		else:
			res = self.binary_search(L, target, low, mid)

		return res



	def run(self):
		self.valid = set()
		# binary search
		for i, x in enumerate(self.L):
			print('progress: {:5.3f}'.format(100.0*i/self.N), end='\r')
			low_idx = self.binary_search(self.L, -10000-x, i+1, self.N)
			j = low_idx
			while self.L[j] + x < 10000 and j < self.N:
				self.valid.add(self.L[j] + x)
				j += 1

		return len(self.valid)

	def test_run(self):
		L = [0, 2, 4, 6, 8, 10]
		# L = self.L
		target = 2
		print(L)
		print('target = ', target)
		res = self.binary_search(L, target, 3, len(L) - 1)
		print(L[res])
		
		return 

if __name__ == '__main__':
	fname = 'hw4.txt'
	S = Solution(fname)
	print(S.run())