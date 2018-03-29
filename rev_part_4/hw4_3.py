#!/usr/bin/env python3

"""
In this assignment we will revisit an old friend, the traveling salesman problem (TSP). 
This week you will implement a heuristic for the TSP, rather than an exact algorithm, 
and as a result will be able to handle much larger problem sizes. Here is a data file 
describing a TSP instance (original source: http://www.math.uwaterloo.ca/tsp/world/bm33708.tsp).

nn.txt
The first line indicates the number of cities. Each city is a point in the plane, and 
each subsequent line indicates the x- and y-coordinates of a single city.

The distance between two cities is defined as the Euclidean distance --- that is, two 
cities at locations (x,y) and (z,w) have distance sqrt((x−z)^2+(y−w)^2) between them.

You should implement the nearest neighbor heuristic:

1. Start the tour at the first city.
2. Repeatedly visit the closest city that the tour hasn't visited yet. In case of a tie, go 
to the closest city with the lowest index. For example, if both the third and fifth cities 
have the same distance from the first city (and are closer than any other city), then the 
tour should begin by going from the first city to the third city.
3. Once every city has been visited exactly once, return to the first city to complete the tour.
In the box below, enter the cost of the traveling salesman tour computed by the nearest 
neighbor heuristic for this instance, rounded down to the nearest integer.
"""
import time
import numpy as np
from  itertools import combinations


class Solution:

	def __init__(self, fname):

		self.V = {}
		with open(fname, 'r') as f:
			self.n = int(f.readline())
			for i, line in enumerate(f.readlines()):
				self.V[i] = (tuple(map(float, line.split()[1:])))

		self.visited = set()

		return None


	def _dist(self, s, t):
		"""
		given two tuple s=(x1, y1) and t=(x2, y2)
		return the distance between s and t
		"""
		return ((s[0] - t[0])**2 + (s[1] - t[1])**2)**0.5

	def find_min(self, s):
		"""
		find the vertex that is closest to the vertex s
		and also unvisited
		"""
		shortest = float('inf')
		to_add = None

		for t in self.V:
			# print(t)
			
			if t in self.visited:
				continue
			
			dist_ = self._dist(self.V[s], self.V[t])
			if dist_ < shortest:
				shortest = dist_
				to_add = t

		return to_add, shortest


	def approx_tsp(self):
		
		res = 0
		v_start = 0
		self.visited.add(v_start)
 
		for i in range(0, self.n-1):
			print('Calculating the approximated TSP, {:,} of total {:,}.....'
				.format(i+1, self.n), end='\r')
			t, dist_ = self.find_min(v_start)
			res += dist_

			v_start = t
			self.visited.add(v_start)
			# print('Shortest distance: ', dist_)
			# print('Add node {}.'.format(v_start))
		
		print('\n')

		# add the last hoop
		res += self._dist(self.V[v_start], self.V[0])

		return res



if __name__ =='__main__':

	t_start = time.time()
	fname = 'nn.txt'
	# fname = 'nn_debug.txt'  # result is 15.2361
	S = Solution(fname)
	res = S.approx_tsp()
	print(res)
	print('Total time taken: {:3.1f} minutes.'.format((time.time() - t_start)/60))







