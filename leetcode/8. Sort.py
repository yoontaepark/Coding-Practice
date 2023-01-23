'''
8. Sort
- 무기: 
    - array랑 통합해도 되는 부분인데 일부 문제만 수록함 
'''
import re
from typing import List, Optional
import collections

# - 문제
#     - (Medium) Leetcode 148. Sort List: https://leetcode.com/problems/sort-list/description/
#     - 풀이: 리스트로 변경 후 sort 하고 다시 역변경, sort 는 웬만하면 내장함수를 쓰는 방향으로 정리 
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # convert linked list to list 
        p = head # assign pointer
        lst = [] # initialize list
        # until pointer reaches to the end, append the value and move pointer to the next
        while p:
            lst.append(p.val)
            p = p.next

        # sort
        lst.sort()

        # convert back list to linked list
        p = head # assign pointer
        # for values in list, assign the value and move pointer to the next
        for value in lst:
            p.val = value
            p = p.next 

        # return head, so that we can have the expected result 
        return head


#     - (Medium) Leetcode 56. Merge Intervals: (https://leetcode.com/problems/merge-intervals/)
#     - 풀이: 하나를 넣고나서 그 다음꺼를 이전것과 비교, 현재기준의 첫 값과 이전것의 마지막값이 겹치면 하나로 합침  
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # assign an empty list
        res = []

        # iterate by sorted intervals 
        for interval in sorted(intervals, key=lambda x: x[0]):
            
            # compare the next interval with result table
            # if next interval's start value is less than or equal to last result's end value
            # merge two lists by replacing max end value
            if res and interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], interval[1]) 

            # add intervals 
            else:
                res += [interval]

        return res    
    
    
#     - (Medium) Leetcode 179. Largest Number: (https://leetcode.com/problems/largest-number/)
#     - 풀이: 삽입정렬 예시, 삽입정렬을 따로 외운다기 보다는 sort pairwise 
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
    

#     - (Medium) Leetcode 973. K Closest Points to Origin: https://leetcode.com/problems/k-closest-points-to-origin/description/
#     - 풀이: 자체 제작 코드, dist를 다 얹은다음에 Sort하고 다시 dist 치우기 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # case 1
        for i, (x, y) in enumerate(points):
            dist = x**2 + y**2
            points[i] += [dist]
        
        return [y[:-1] for y in sorted(points, key=lambda x: x[-1])[:k]]    
    
        # # case 2: similar approach, but uses heapq
        # heap = []
        # for (x, y) in points:
        #     dist = x**2 + y**2
        #     heapq.heappush(heap, (dist, x, y))

        # res = []
        # for _ in range(k):
        #     (dist, x, y) = heapq.heappop(heap)
        #     res.append((x,y))

        # return res
        