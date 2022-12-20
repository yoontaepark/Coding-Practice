'''
1. Array
- 무기: 
    - 
'''
import re
from typing import List

# - 문제
#     - (Easy) Leetcode 1. Two Sum: (https://leetcode.com/problems/two-sum/)
#     - 풀이: we can do brute force, but it will take O(n^2) time complexity. 
#     - therefore, we use target-num vs nums_map strategy
#     - two pointer method will be used in three-sum, not here as we are trying to get index of the list 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # assuming there is one number that can be add up to target, we try to find another number
        # reassigning (index, value) pair in the list
        # initialize a dictionary
        nums_map = {}

        # update dictionary as (value, index) pair
        for i, num in enumerate(nums):
            nums_map[num] = i

        # now, try to find another number
        # for each number in nums list, we compare nums_map key with target-num, 
        # and return the value of nums_map which is the index of the nums list 
        # also, add i != nums_map's value to make sure that we are not using i twice 
        for i, num in enumerate(nums):
            if target-num in nums_map and i != nums_map[target-num]:
                return [i, nums_map[target-num]]

