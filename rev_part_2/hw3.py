#!/usr/bin/env python3

"""
The goal of this problem is to implement the "Median Maintenance" algorithm (covered in the Week 3 
lecture on heap applications). The text file contains a list of the integers from 1 to 10000 in unsorted order; 
you should treat this as a stream of numbers, arriving one by one. Letting xi denote the ith number of the file, 
the kth median mk is defined as the median of the numbers x1,…,xk. (So, if k is odd, then mk is ((k+1)/2)th smallest 
number among x1,…,xk; if k is even, then mk is the (k/2)th smallest number among x1,…,xk.)

In the box below you should type the sum of these 10000 medians, modulo 10000 (i.e., only the last 4 digits). 
That is, you should compute (m1+m2+m3+⋯+m10000)mod10000.
"""

from heapq import heappush, heappop

class Solution(object):

	def __init__(self):
		return

	def stream(self, fname):
		
		with open(fname, 'r') as f:
			while True:
				line = f.readline()
				if not line:
					break
				yield int(line.strip())

	def get_median(self, fname):

		# first initate the low and high
		tmp = []
		running_median = []
		for i, x in enumerate(self.stream(fname)):
			if i == 0:
				running_median.append(x)
			if i >= 2:
				break
			tmp.append(x)
		
		low, high = [-1*min(tmp)], [max(tmp)]	# two heaps for the lower and higher half
		running_median.append(-1*low[0])

		for i, x in enumerate(self.stream(fname)):
			if i < 2:
				continue

			# case 1, low and high is equal length
			if len(low) - len(high) == 0:
				if x < high[0]: 
					heappush(low, -1*x)
					running_median.append(-1*low[0])
				else:
					heappush(high, x)
					running_median.append(high[0])
				
				continue
			# case 2, low has one more element than high
			if len(low) - len(high) == 1:
				if x < high[0]:
					heappush(low, -1*x)
					tmp = -1*heappop(low)
					heappush(high, tmp)
				else:
					heappush(high, x)
				
				running_median.append(-1*low[0])
				continue
			# case 3, high has one more element than low
			if len(low) - len(high) == -1:
				if x < high[0]:
					heappush(low, -1*x)
				else:
					heappush(high, x)
					tmp = heappop(high)
					heappush(low, -1*tmp)

				running_median.append(-1*low[0])
				continue
			else:
				print('Error!')

		# print('low: ', low)
		# print('high: ', high)
		# print('running_median: ', running_median)
		result = sum(running_median) % 10000 
		print(result)

		return result

if __name__ == '__main__':

	S = Solution()
	S.get_median('hw3.txt')
