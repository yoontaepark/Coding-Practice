'''
5. hash table
- 무기: 
    - 사실 무기랄건 없고 dict-key에 value가 추가되는 개념으로 보면 될 거 같음
'''
import re
from typing import List, Optional
import collections

#     - Q2. (Medium) Leetcode 771. Jewels and Stones: (https://leetcode.com/problems/jewels-and-stones/)
#     - 풀이: 너무 좋은 문제, collections.Counter 뿐만 아니라, one liner 풀이도 기억하기 
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # case1: use collection.Counter
        freq = collections.Counter(stones)
        res = 0
        # as jewels have unique values, we can check each values and add the frequency 
        for key in jewels:
            res += freq[key]
        return res

        # case2: one liner: s in condition for s in list(string)
        # return sum(s in jewels for s in stones)
    
    
#     - Q3. (Medium) Leetcode 3. Longest Substring Without Repeating Characters: 
#       (https://leetcode.com/problems/longest-substring-without-repeating-characters)
#     - 풀이: 너무 좋은 문제, dict + two pointers (with one as an index)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0 # initialize as zero, in case of null string s

        # here, we will be using two pointers (one with index, one with start)
        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1 # We need to restart counting substring, so add +1 to assign start 
            else:
                max_length = max(max_length, index-start+1) # just update max length 

            used[char] = index # always assgin index
        
        # final result
        return max_length
                
                
#     - Q4. (Medium) Leetcode 347. Top K Frequent Elements: (https://leetcode.com/problems/top-k-frequent-elements)
#     - 풀이: most_common 쓰고 * unpack 한다음에 zip으로 앞에꺼만 모으기, 그 후에 [0]만 리턴 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # using * (unpack) + zip
        return list(zip(*collections.Counter(nums).most_common(k)))[0]
                     