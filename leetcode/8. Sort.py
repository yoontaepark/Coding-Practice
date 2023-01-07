'''
8. Sort
- 무기: 
    - array랑 통합해도 되는 부분인데 일부 문제만 수록함 
'''
import re
from typing import List, Optional
import collections

# - 문제
#     - (Medium) Leetcode 179. Largest Number: (https://leetcode.com/problems/largest-number/)
#     - 풀이: 삽입정렬 예시라고 생각 

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # start with 1
        i = 1

        # iterate until i gets to the end index
        while i < len(nums):

            # we will be using j as another pointer
            j = i

            # compare each pair of numbers by stringwise adding i + i-1 vs i-1 + i
            # if righthand side is larger, and j > 0, we can swap values 
            # continue this pairwise comparision by decreaisng j
            while j > 0 and (str(nums[j-1]) + str(nums[j])) < (str(nums[j]) + str(nums[j-1])):
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
            
            # we want to repeat this by adding i + 1
            i += 1
        
        # return numbers by converting to string -> int -> string 
        return str(int(''.join(map(str, nums))))
