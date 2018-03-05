#!/usr/bin/env python3
"""
This file describes a set of jobs with positive and integral weights and lengths. It has the format

[number_of_jobs]

[job_1_weight] [job_1_length]

[job_2_weight] [job_2_length]

...

For example, the third line of the file is "74 59", indicating that the second job has weight 74 
and length 59.

You should NOT assume that edge weights or lengths are distinct.

Your task in this problem is to run the greedy algorithm that schedules jobs in decreasing order 
of the difference (weight - length). Recall from lecture that this algorithm is not always optimal. 
IMPORTANT: if two jobs have equal difference (weight - length), you should schedule the job with 
higher weight first. Beware: if you break ties in a different way, you are likely to get the wrong 
answer. You should report the sum of weighted completion times of the resulting schedule.

We will also cover the second question here too: 
Your task now is to run the greedy algorithm that schedules jobs (optimally) in decreasing order of 
the ratio (weight/length). In this algorithm, it does not matter how you break ties. You should 
report the sum of weighted completion times of the resulting schedule
"""

class Solution(object):
	
	def __init__(self, fname):
		with open(fname, 'r') as f:
			self.N = f.readline()
			self.L = []  # list of tuple (weight, length, w - l, w/l)
			for line in f.readlines():
				w, l = list(map(int, line.split()))
				self.L.append((w, l, w - l, 1.0*w/l))

	def completion_time(self, L):
		# given a schedule list L, return the weighted completion times
		running_sum = 0
		running_time = 0
		for tuple_ in L:
			running_time += tuple_[1]
			running_sum += running_time * tuple_[0]

		return running_sum

	def run_1(self):
		# first run, with descending order of (w-l)
		self.L.sort(key=lambda x: (x[2], x[0]), reverse=True)
		res = self.completion_time(self.L)
		print('The weighted completion time of run 1 is: {}'.format(res))

	def run_2(self):
		# second run, with descending order of w/l
		self.L.sort(key=lambda x: x[3], reverse=True)
		res = self.completion_time(self.L)
		print('The weighted completion time of run 2 is: {}'.format(res))



if __name__ == '__main__':
	fname = 'hw1_1.txt'
	S = Solution(fname)
	S.run_1()
	S.run_2()
