'''
9. Binary_search
- 무기: 
    - array랑 통합해도 되는 부분인데 일부 문제만 수록함 
'''
import re
from typing import List, Optional
import collections

# - 문제
#     - (Medium) Leetcode 704. Binary Search: https://leetcode.com/problems/binary-search/description/
#     - 풀이: for recursive function, you can run the function and return the saved res, or just return the function that contatins the res
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # using binary search 
        def binary_search(left, right):
            # until left gets right 
            if left <= right:
                # get mid and compare. based on the number and target, make a recursive function 
                mid = (left + right) // 2
                if nums[mid] < target:
                    return binary_search(mid+1, right)
                elif nums[mid] > target: 
                    return binary_search(left, mid-1)
                else:
                    return mid

            # in case it doesn't have any number that matches the target 
            else: 
                return -1

        # using recursive function
        return binary_search(0, len(nums)-1)
    

#     - (Medium) Leetcode 33. Search in Rotated Sorted Array: (https://leetcode.com/problems/search-in-rotated-sorted-array/description/)
#     - 풀이: used iteration instead of recursion. Note that we can use any of the function we want 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find min value's index, this will be added as a pivot index 

        # 0 1 2 4 5 6 7 = idx (3 + 4) % 7
        # 4 5 6 7 0 1 2 = idx 0 
        # for 0, from sorted list, we need to move 4 (index 0 -> index 4)

        # calculating pivot: find argmin in python list 
        pivot = nums.index(min(nums))

        nums.sort()

        # use binary search, as algorithm need O(log n) runtime
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return (mid + pivot) % len(nums)

        return -1
    
    
#     - (Medium) Leetcode 349. Intersection of Two Arrays: https://leetcode.com/problems/intersection-of-two-arrays/description/
#     - 풀이: using two pointers
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # using two pointers
        res = set()

        # sort both lists
        nums1.sort()
        nums2.sort()

        # initialize both pointers as 0, and move both from left to right
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else: 
                res.add(nums1[i])
                i += 1
                j += 1

        return res    
    

#     - (Medium) Leetcode 167. Two Sum II - Input Array Is Sorted: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
#     - 풀이: using two pointers again
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers
        left, right = 0, len(numbers)-1

        while left < right: 
            sums = numbers[left] + numbers[right]
            if sums < target:
                left += 1
            elif sums > target:
                right -= 1
            else:
                return [left+1, right+1]    
            

#     - (Medium) Leetcode 240. Search a 2D Matrix II: https://leetcode.com/problems/search-a-2d-matrix-ii/description/
#     - 풀이: using any function in python, also use list comprehension 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # use any function in python 
        return any([target in row for row in matrix])
            