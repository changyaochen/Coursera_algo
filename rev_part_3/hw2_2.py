#!/usr/bin/env python3

"""
In this question your task is again to run the clustering algorithm from lecture, 
but on a MUCH bigger graph. So big, in fact, that the distances (i.e., edge costs) 
are only defined implicitly, rather than being provided as an explicit list.

The format is:

[# of nodes] [# of bits for each node's label]

[first bit of node 1] ... [last bit of node 1]

[first bit of node 2] ... [last bit of node 2]

...

For example, the third line of the file "0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1" 
denotes the 24 bits associated with node #2.

The distance between two nodes u and v in this problem is defined as the Hamming distance 
--- the number of differing bits --- between the two nodes' labels. For example, the Hamming 
distance between the 24-bit label of node #2 above and the label 
"0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1"
"0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1" is 3 
(since they differ in the 3rd, 7th, and 21st bits).

The question is: what is the largest value of k such that there is a k-clustering with 
spacing at least 3? That is, how many clusters are needed to ensure that no pair of nodes 
with all but 2 bits in common get split into different clusters?

NOTE: The graph implicitly defined by the data file is so big that you probably 
can't write it out explicitly, let alone sort the edges by cost. So you will have to be a 
little creative to complete this part of the question. For example, is there some way you 
can identify the smallest distances without explicitly looking at every pair of nodes?
"""
from UnionFind import UnionFind
import time

class Solution:

	def __init__(self, fname):

		self.V_bin = set()
		self.V = set()

		with open(fname, 'r') as f:
			self.N, self.bit = list(map(int, f.readline().split()))
			for line in f.readlines():
				bin_repr = (''.join(line.split()))
				
				self.V_bin.add(bin_repr)
				self.V.add(int(bin_repr, 2))


	def Hamming(self, num, bit=24):
		# return a dict of numbers with Hamming distance of 1 from number
		res = {}
		mask = 1  # this is the mask
		for _ in range(bit):
			res[num ^ mask] = True  # bit wise xor, to flip one bit
			mask = mask << 1  # bit shifted to left

		return res

	
	def Hamming_set(self, num, dist=2):
		# return a set of numbers that has Hamming distance <= dist
		res = {num: True}
		for _ in range(dist):
			tmp_keys = list(res.keys())
			for n in tmp_keys:
				res.update(self.Hamming(num=n, bit=self.bit))

		del res[num]  # remove the original number
		return res

	def run(self):
		# init a UnionFind structure
		X = UnionFind()
		for v in self.V:
			X[v]

		k = len(self.V)  # init the number of cluster
		for i, v in enumerate(self.V):
			print('Processing vertex {} of total {}...'.format(i, self.N), end='\r')
			to_merge = self.Hamming_set(v, dist=2)  # find all the values with Hamming distance <= 2
			for c in to_merge:
				if c in self.V and X[v] != X[c]: 
					X.union(v, c)  # merge, i.e. union!
					k -= 1
 
		print('\n', k)


if __name__ == '__main__':
	t_start = time.time()
	fname = 'hw2_2.txt'
	S = Solution(fname)
	S.run()
	print('Time elasped: {:6.3f} seconds.'.format(time.time() - t_start))




	