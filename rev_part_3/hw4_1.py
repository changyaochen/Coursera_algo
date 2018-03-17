#!/usr/bin/env python3

"""
In this programming problem and the next you'll code up the knapsack algorithm from lecture.

Let's start with a warm-up. Download the text file below.

knapsack1.txt
This file describes a knapsack instance, and it has the following format:

[knapsack_size][number_of_items]

[value_1] [weight_1]

[value_2] [weight_2]

...

For example, the third line of the file is "50074 659", indicating that the second item has value 
50074 and size 659, respectively.

You can assume that all numbers are positive. You should assume that item weights and the knapsack 
capacity are integers.

In the box below, type in the value of the optimal solution.
"""

class Solution:

	def __init__(self, fname):

		self.V, self.W = {}, {}
		with open(fname, 'r') as f:
			self.n_W, self.n_n = list(map(int, f.readline().split()))

			for i, line in enumerate(f.readlines()):
				self.V[i-1] = (int(line.split()[0]))
				self.W[i-1] = (int(line.split()[1]))

	def knapsack(self):
		dp_last = [0]*(1+self.n_W)  # dynamic programming array
		dp = [0]*(1+self.n_W)  # dynamic programming array		

		# main dp loop
		for i in range(self.n_n):
			for w in range(1+self.n_W):
				# check for the value without item i
				if self.W[i] > w:
					with_item = 0
				else:
					with_item = dp_last[w - self.W[i]] + self.V[i]
				
				dp[w] = max(dp_last[w], with_item)
			
			dp_last = dp[:]
			print(dp)
		
		print('The maximum value is {}.'.format(dp[-1]))	
		
		return dp[-1]

	def knapsack_2(self):
		# one dp array, update from back
		dp = [0]*(1+self.n_W)  # dynamic programming array		

		# main dp loop
		for i in range(self.n_n):
			print('Processing {} of total {}'.format(i, self.n_n), end='\r')
			for w in range(self.n_W, -1, -1):
				# check for the value without item i
				if self.W[i] > w:
					with_item = 0
				else:
					with_item = dp[w - self.W[i]] + self.V[i]
				
				dp[w] = max(dp[w], with_item)
			
			# print(dp)
		
		print('The maximum value is {}.'.format(dp[-1]))	
		
		return dp[-1]

	def knapsack_3(self):
		# one dp dict, update from back
		dp = {w: 0 for w in range(1+self.n_W)}  # dynamic programming array		

		# main dp loop
		for i in range(self.n_n):
			print('Processing {} of total {}'.format(i, self.n_n), end='\r')
			for w in range(self.n_W, -1, -1):
				# check for the value without item i
				if self.W[i] > w:
					with_item = 0
				else:
					with_item = dp[w - self.W[i]] + self.V[i]
				
				dp[w] = max(dp[w], with_item)
			
			# print(dp)
		
		print('The maximum value is {}.'.format(dp[self.n_W]))	
		
		return dp[self.n_W]


if __name__ == '__main__':
	fname = 'hw4_2.txt'
	S = Solution(fname)
	S.knapsack_3()

	




	