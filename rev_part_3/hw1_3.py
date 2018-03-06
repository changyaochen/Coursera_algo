#!/usr/bin/env python3
"""
This file describes an undirected graph with integer edge costs. It has the format

[number_of_nodes] [number_of_edges]

[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]

[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]

...

For example, the third line of the file is "2 3 -8874", indicating that there is an edge connecting vertex 
#2 and vertex #3 that has cost -8874.

You should NOT assume that edge costs are positive, nor should you assume that they are distinct.

Your task is to run Prim's minimum spanning tree algorithm on this graph. You should report the overall cost 
of a minimum spanning tree --- an integer, which may or may not be negative --- in the box below.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Prim's 
algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing a 
heap-based version. The simpler approach, which should already give you a healthy speed-up, is to maintain 
relevant edges in a heap (with keys = edge costs). The superior approach stores the unprocessed vertices in 
the heap, as described in lecture. Note this requires a heap that supports deletions, and you'll probably need 
to maintain some kind of mapping between vertices and their positions in the heap.
"""

class Solution(object):
	
	def __init__(self, fname):
		self.G = {}
		with open(fname, 'r') as f:
			self.n, self.m = f.readline().split()
			for line in f.readlines():
				n1, n2, cost = list(map(int, line.split()))
				# process n1
				if n1 not in self.G:
					self.G[n1] = [(n2, cost)]
				else:
					self.G[n1].append((n2, cost))
				# process n2
				if n2 not in self.G:
					self.G[n2] = [(n1, cost)]
				else:
					self.G[n2].append((n1, cost))

	def run1(self):
		# vanilla implementation of Prim's algorithm with O(mn) time
		visited = set()
		MST_cost = 0

		# visit a random first node
		start = list(self.G.keys())[0]
		visited.add(start)

		
		# main loop
		while len(visited) < len(self.G):
			tmp_min = float('inf')
			candidate = -1

			# find next node to absorbe
			for node in visited:
				for end, cost in self.G[node]:
					if end not in visited: 
						if cost < tmp_min:
							tmp_min, candidate = cost, end

			visited.add(candidate)
			MST_cost += tmp_min

		return MST_cost




if __name__ == '__main__':
	fname = 'hw1_3.txt'
	S = Solution(fname)
	print('MST cost is: {}'.format(S.run1()))

