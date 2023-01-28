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
            
# 76. Minimum Window Substring: https://leetcode.com/problems/minimum-window-substring/description/            
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # create a dictionary on t
        word_list = collections.Counter(t)
        # missing word count
        missing = len(t)
        # initialization of start,end and left. right will be moving by iteration 
        start = end = left = 0

        # checking word with right pointer. right pointer will move forward from 1
        for right, word in enumerate(s, 1):
            # for every iteration, check if given word is in word list. Then -1 for missing
            # for word list, -1 as well. As we are using collections.Counter function, 
            # unseen word will be counted as 0 so the result would be -1 
            missing -= word_list[word]>0 
            word_list[word] -= 1
            
            # if missing arrives to 0, then we update below 
            if missing == 0:
                # left pointer checker: if given left pointer is not a target word, move 
                while left < right and word_list[s[left]]<0:
                    word_list[s[left]] += 1
                    left += 1

                # start, end point update
                if not end or right-left < end-start:
                    start, end = left, right

                # general update: moving left pointers
                word_list[s[left]] += 1
                missing += 1
                left += 1

        # return final result        
        return s[start:end]


# 424. Longest Repeating Character Replacement: sliding window with two pointers 
# make sure you understand that right-left-most_common = k, and if left_side > right_side, need to move pointers 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # find index right/left where max(right) - min(left) + 1 - most_common_cnt <= k
        # then return right - left + 1 
        # i.e AAAAB, k=2, we can set 4-0+1-4 <= 2, and return 4-0+1 = 5
        # if k=0, then we can't change B, so we cannot return 5, but 4

        # initialize pointers, and dict for most_common
        left = 0
        cnt = collections.Counter()

        # then move right pointer
        for right in range(len(s)):

            # for each right pointer, add string count
            cnt[s[right]] += 1

            # then calculate most_common count 
            # as most_common returns i.e. ((a,2)), we get 2 by [0][1]
            most_common_cnt = cnt.most_common(1)[0][1] 

            # move left pointer, if needed change is greater than k
            # we don't need to save max count, as we are both moving left and right pointers at once
            if right - left + 1 - most_common_cnt > k:
                cnt[s[left]] -= 1
                left += 1

        # after checking all pointers, return final result
        return right - left + 1            