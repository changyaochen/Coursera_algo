#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 21:18:59 2018

@author: changyaochen

The file contains the adjacency list representation of a simple undirected
 graph. There are 200 vertices labeled 1 to 200. The first column in the 
 file represents the vertex label, and the particular row (other entries 
 except the first column) tells all the vertices that the vertex is adjacent
 to. So for example, the 6th row looks like : "6	155	56	52	120	......". This
 just means that the vertex with label 6 is adjacent to (i.e., shares an 
 edge with) the vertices with labels 155,56,52,120,......,etc

Your task is to code up and run the randomized contraction algorithm for 
the min cut problem and use it on the above graph to compute the min cut. 
(HINT: Note that you'll have to figure out an implementation of edge 
contractions. Initially, you might want to do this naively, creating a new 
graph from the old every time there's an edge contraction. But you should 
also think about more efficient implementations.) (WARNING: As per the 
video lectures, please make sure to run the algorithm many times with 
different random seeds, and remember the smallest cut that you ever find.) 
Write your numeric answer in the space provided. So e.g., if your answer 
is 5, just type 5 in the space provided.
"""
import random

class Solution():

    
    def __init__(self, fname):
        # we are going to repr the graph with dict
        self.G = {}
        with open(fname, 'r') as f:
            lines = f.readlines()
            for line in lines:
                tmp = list(map(int, line.split('\t')[1:-1]))  # last char is \n
                v = int(line.split('\t')[0])
                self.G[v] = [x for x in tmp if x != v]  # remove self loop
    
    def shrink(self, s, t):
        # s will be the winner, t will be eliminated
        # need to update the rest of the graph to replace t with s
        for node in self.G[t]:
            self.G[node] = [s if x == t else x for x in self.G[node]]
        
        # need to remove the connecting edges and self loop
        tmp = self.G[s] + self.G[t]
        self.G[s] = [x for x in tmp if x not in [s, t]]
               
        # now remove the node
        del self.G[t]
        
        
    def karger(self):
        while len(self.G) > 2:
            # randomly pick two vortice
            pool = list(self.G.keys())
            s = random.choice(pool)
            # t needs to be connected to 
            t = random.choice(self.G[s])
            while s == t:
                t = random.choice(list(slef.G[s].values()))
            self.shrink(s, t)
        tmp = (list(map(len, self.G.values())))
        assert(min(tmp) == max(tmp))
    
        return min(tmp)
        
                
if __name__ == '__main__':
    fname = 'wk4.txt'
    min_ = float('inf')
    N = 100
    for i in range(N):
        S = Solution(fname)
        min_ = min(min_, S.karger())
        print('{}: {}'.format(i, min_))
    print(min_)
    