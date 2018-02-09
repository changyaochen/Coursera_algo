#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 22:56:19 2018

@author: Changyao Chen

this is for Karatsuba multiplication implementation
"""
import random

class Solution():
    def karatsuba(self, a, b):
        # base case:
        if int(a) == 0 or int(b) == 0:
            return 0
        if len(str(a)) == 1 or len(str(b)) == 1:
            return a*b
        
        # recursive calls
        n = max(len(str(a)), len(str(b)))
        m = n - n//2
        
        a_left, a_right = a//10**m, a%10**m
        b_left, b_right = b//10**m, b%10**m
        
        part_1 = self.karatsuba(a_left, b_left)
        part_2 = self.karatsuba(a_right, b_right)
        part_3 = self.karatsuba((a_left + a_right), (b_left + b_right)) - part_1 - part_2
        
        return 10**(2*m)*part_1 + part_2 + 10**m*part_3
        
if __name__ == '__main__':
    S = Solution()
    x, y = random.randint(0, 1e64), random.randint(0, 1e64)
    assert(x*y == S.karatsuba(x, y))
    
    
    
  
    
