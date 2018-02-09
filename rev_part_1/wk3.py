#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Your task is to compute the total number of comparisons used to sort the 
given input file by QuickSort. As you know, the number of comparisons 
depends on which elements are chosen as pivots, so we'll ask you to explore 
three different pivoting rules.

You should not count comparisons one-by-one. Rather, when there is a 
recursive call on a subarray of length m, you should simply add m−1 to 
your running total of comparisons. (This is because the pivot element 
is compared to each of the other m−1 elements in the subarray in this 
recursive call.)
"""

class Solution():
    
    def __init__(self, fname):
        with open(fname, 'r') as f:
            self.data = list(map(int, f.readlines()))
        self.count = 0
    
    # ===== using first element as pivot =====
    def quick_sort_1(self, array, left, right):
        if left >= right:
            return 
        pivot = array[left]  # first element as pivot
        i, j = left + 1, left + 1  # i is the pointer to the first 'large portion'
        for j in range(left+1, right+1):
            if array[j] < pivot:
                array[i], array[j] = array[j], array[i]  # swap
                i += 1
        self.count += right - left
            
        # put the pivot the it rightful position
        array[left], array[i-1] = array[i-1], array[left]
        self.quick_sort_1(array, left, i-2)  # left call
        self.quick_sort_1(array, i, right)  # right call
    
    def run_1(self):
        self.quick_sort_1(self.data, 0, len(self.data)-1)
        
        
    # ==== using the last one, but recurse to the firt method ====
    def quick_sort_2(self, array, left, right):
        if left >= right:
            return
        
        #swap left and right
        array[left], array[right] = array[right], array[left]         
        pivot = array[left]  # first element as pivot
        i, j = left + 1, left + 1  # i is the pointer to the first 'large portion'
        for j in range(left+1, right+1):
            if array[j] < pivot:
                array[i], array[j] = array[j], array[i]  # swap
                i += 1
        self.count += right - left
            
        # put the pivot the it rightful position
        array[left], array[i-1] = array[i-1], array[left]
        self.quick_sort_2(array, left, i-2)  # left call
        self.quick_sort_2(array, i, right)  # right call
    
    def run_2(self):
        self.quick_sort_2(self.data, 0, len(self.data)-1)
        
    # ===== now pick the pivot more carfully =====
    def quick_sort_3(self, array, left, right):
        
        if left >= right:
            return
        mid = (left + right) // 2  
        
        # if the mid one is median
        if array[mid] < max(array[left], array[right]) \
                and array[mid] > min(array[left], array[right]):
            # swap
            array[mid], array[left] = array[left], array[mid]
        
        # if the right one is median
        elif array[right] < max(array[left], array[mid]) \
                and array[right] > min(array[left], array[mid]):
            #swap
            array[left], array[right] = array[right], array[left]
        
        pivot = array[left]  # first element as pivot
        i, j = left + 1, left + 1  # i is the pointer to the first 'large portion'
        for j in range(left+1, right+1):
            if array[j] < pivot:
                array[i], array[j] = array[j], array[i]  # swap
                i += 1
        self.count += right - left
        
        # put the pivot the it rightful position
        array[left], array[i-1] = array[i-1], array[left]
        self.quick_sort_3(array, left, i-2)  # left call
        self.quick_sort_3(array, i, right)  # right call
        
    def run_3(self):
        self.quick_sort_3(self.data, 0, len(self.data)-1)
        
                           
            
if __name__ == '__main__':
    S = Solution('wk3.txt')
    S.run_1()
    l = S.data
    print(S.count)
