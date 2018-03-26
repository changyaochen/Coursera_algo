#!/usr/bin/env python3

"""
In this assignment you will implement one or more algorithms for the traveling salesman problem, 
such as the dynamic programming algorithm covered in the video lectures. Here is a data file 
describing a TSP instance.

tsp.txt
The first line indicates the number of cities. Each city is a point in the plane, and each subsequent 
line indicates the x- and y-coordinates of a single city.

The distance between two cities is defined as the Euclidean distance --- that is, two cities at locations 
(x,y) and (z,w) have distance sqrt[(x−z)^2+(y−w)^2] between them.

In the box below, type in the minimum cost of a traveling salesman tour for this instance, rounded 
down to the nearest integer.
"""
import time
import numpy as np
from  itertools import combinations


class Solution:

	def __init__(self, fname):

		self.V = []
		with open(fname, 'r') as f:
			self.n = int(f.readline())
			for i, line in enumerate(f.readlines()):
				self.V.append(tuple(map(float, line.split())))

		# to get all the edges, in matrix form
		self.G = np.ndarray(shape=(self.n, self.n), dtype=float)
		for i in range(self.n):
			for j in range(self.n):
				self.G[i, j] = self._dist(self.V[i], self.V[j])

		return None


	def _dist(self, s, t):
		"""
		given two tuple s=(x1, y1) and t=(x2, y2)
		return the distance between s and t
		"""
		return ((s[0] - t[0])**2 + (s[1] - t[1])**2)**0.5


	def _all_subsets(self, all_, m, include=0):
		"""
		given a set of items <set> all_,
		return the list of its subsets with size <int> m 

		additionally, we want the include item in the subsets
		"""

		res = []
		for x in combinations(all_, m):
			if include in x:
				res.append(set(x))

		return res

	def _set_2_str(self, set_in):
		"""
		given a <set> set_in, make a unique identifier to it
		"""
		length = len(str(self.n))
		L = list(map(str, sorted(list(set_in))))

		identifier = ''.join([x.zfill(length) for x in L])

		return identifier


	def _subset_idx_map(self):
		"""
		make the index mapping for each eligible subset 
		"""
		t_start = time.time()
		count = 0
		
		self.mapping = {self._set_2_str({0}): count}  # the idx for the start vertex
		count += 1

		for i in range(2, self.n+1):
			S = self._all_subsets(set(range(self.n)), i)
			print('Making subset indices, step {} of {}... number of subsets: {:,}        '
				.format(i, self.n, len(S)), end ='\r')
			for s in S:
				self.mapping[self._set_2_str(s)] = count
				count += 1
		print('\nTotal time taken: {:6.1f} minutes.'
			.format((time.time() - t_start)/60))

		return None

	def tsp(self):
		# dp solution for tsp

		t_start = time.time()

		# the 2D dp array
		# indexed by subsets S ⊆ {0,1,...,n-1} that contain 0 and destinations j ∈ {0,1,...,n-1}
		# the size for A will be 2^(n-1) * n
		self._subset_idx_map()  # make the mapping
		self.A = np.full(shape=(len(self.mapping), self.n), fill_value=float('inf'))

		# base case
		self.A[self.mapping[self._set_2_str({0})], 0] = 0

		# main dp loop
		for m in range(2, self.n+1):  # size of S
			print('\nstep {} of total of {}....'.format(m, self.n))
			# process all the subsets with size m
			total_subsets = len(self._all_subsets(set(range(self.n)), m)) 
			for ii, S in enumerate(self._all_subsets(set(range(self.n)), m)):  # get all the subsets with size m
				print('===> processing subset {:,} of total {:,}...'.format(ii+1, total_subsets), end='\r')
				for j in S:  # for each vertex j in a subset S
					if j == 0:  # that's the start vertex
						pass
					else:
						prev = {x for x in S if x != j}  # the set without vertex j
						# print('prev: ', prev)
						candidates = []

						# loop through all possible cases
						for k in range(self.n):
							if k == j: 
								pass
							else:
								tmp_dist = self.A[self.mapping[self._set_2_str(prev)], k] + self.G[k, j]
								candidates.append(tmp_dist)
						# print(candidates)
						self.A[self.mapping[self._set_2_str(S)], j] = min(candidates)

		# final pass
		res = float('inf')
		for j in range(1, self.n):
			# will go through the last row of the 2D array
			# last row corresponds the full set
			res = min(res, self.A[-1, j] + self.G[j, 0])

		print('\nDone! The total time taken is {:5.1f} minutes.'
			  .format((time.time() - t_start)/60))
		print(' The result is: {}'.format(res))
		return res



if __name__ =='__main__':
	fname = 'tsp.txt'
	# fname = 'tsp_debug_3.txt'
	S = Solution(fname)
	res = S.tsp()







