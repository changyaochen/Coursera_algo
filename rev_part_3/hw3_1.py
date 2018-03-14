#!/usr/bin/env python3

"""
In this programming problem and the next you'll code up the greedy algorithm from the lectures on Huffman coding.

Download the text file below.

huffman.txt
This file describes an instance of the problem. It has the following format:

[number_of_symbols]

[weight of symbol #1]

[weight of symbol #2]

...

For example, the third line of the file is "6852892," indicating that the weight of the second symbol of 
the alphabet is 6852892. (We're using weights instead of frequencies, like in the "A More Complex Example" video.)

Your task in this problem is to run the Huffman coding algorithm from lecture on this data set. What is 
the maximum length of a codeword in the resulting Huffman code?
"""

from heapq import heapify, heappush, heappop

class Solution:

	def __init__(self, fname):

		self.W = []
		self.L = {}

		with open(fname, 'r') as f:
			self.N = f.readline()
			for i, line in enumerate(f.readlines()):
				self.W.append((int(line), [i]))
				self.L[i] = 0

		heapify(self.W)

	def run(self):

		while len(self.W) > 1:
			w_1, s_1  = heappop(self.W)
			w_2, s_2 = heappop(self.W)
			for s in s_1:
				self.L[s] += 1
			for s in s_2:
				self.L[s] += 1
			
			heappush(self.W, ((w_1 + w_2), (s_1 + s_2)))

		print('Maximum length is: {}.'.format(max(list(self.L.values()))))
		print('Minimum length is: {}.'.format(min(list(self.L.values()))))

		return


if __name__ == '__main__':
	fname = 'hw3_1.txt'
	S = Solution(fname)
	S.run()
	




	