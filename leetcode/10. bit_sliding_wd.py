'''
10. bit_manipul
- 무기: 
    - 2의 보수는 일단 제끼고, xor 같은거부터 챙겨두기
'''
import re
from typing import List, Optional
import collections

# - 문제
#     - (Medium) Leetcode 
#     - 풀이: use ^ symbol as a XOR symbol

# 136. Single Number: https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # case 1: using ^(XOR) symbol
        # 0^0^0^...^4(only number that appears not twice)
        # for rest of numbers, (say 1^1) they are all cancelled out (result is 0)
        result = 0
        for num in nums:
            result ^= num
        return result
        
        # # case2: set of all numbers * 2 - sum of all numbers 
        # return sum(set(nums))*2 - sum(nums)
        
        
# 461. Hamming Distance: https://leetcode.com/problems/hamming-distance/description/
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # change into bitwise and the result will be in a string format '0b///'
        # then, we count '1' 
        return bin(x^y).count('1')        
    
    
# 191. Number of 1 Bits: https://leetcode.com/problems/number-of-1-bits/    
class Solution:
    def hammingWeight(self, n: int) -> int:
        # same question 461 (hamming dist)
        return bin(n^0).count('1')    
    

'''
10-2. sliding window
- 무기: 
    - two pointer 의 다른 버젼, 길이가 고정된 two pointer라고 생각하자 
'''    

# 239. Sliding Window Maximum: https://leetcode.com/problems/sliding-window-maximum/description/
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = collections.deque()
        res = []

        # for each index 
        for i in range(len(nums)):

            # when moving the window, make sure to remove leftmost prev index
            if deq and i-deq[0] == k:
                deq.popleft()

            # before adding current index, check and remove all the remaining values that are smaller than current
            while deq and nums[deq[-1]] <= nums[i]:
                deq.pop()

            # we basically add index into deq
            deq.append(i)

            # then we append the max deq. However, as max function gets an TLE
            # we put the max value index in deq[0] and append the result
            if i+1 >= k:
                res.append(nums[deq[0]])

        # return the result
        return res
            