"""
This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) 
in some order, with no integer repeated.

Your task is to compute the number of inversions in the file given, 
where the  row of the file indicates the  entry of an array.

Because of the large size of this array, you should implement 
the fast divide-and-conquer algorithm covered in the video lectures.

The file is named 'wk2.txt', resides in the same folder.
"""

class Solution():
    
    def __init__(self, fname):
        self.count = 0
        with open(fname, 'r') as f:
            lines = f.readlines()
        self.array = list(map(int, lines)) 
    
    def merge(self, left, right):
        i, j, m, n = 0, 0, len(left), len(right)
        merged = []
        while i < m and j < n:
            if left[i] < right[j]:  # left element is smaller
                merged.append(left[i])
                i += 1
            else:  # left element is larger, there will be one inversion
                merged.append(right[j])
                j += 1
                self.count += (m-i)  # every element to the right of left[i] count for an inversion
            
        merged.extend(left[i:])  # left array has elements left
        merged.extend(right[j:])  # right array has elements left
        
        return merged
    
    def merge_sort(self, array):
        if len(array) <= 1:
            return array
        n = len(array)
        left, right = self.merge_sort(array[:n//2]), self.merge_sort(array[n//2:])
        return self.merge(left, right)
    
    def run(self):
        return self.merge_sort(self.array)

if __name__ == '__main__':
    fname = 'wk2.txt'
    S = Solution(fname)
    sorted_ = S.run()
    print(S.count)
    