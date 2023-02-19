'''
2. Array
- 무기: 
    - two sum 같은 경우에는: target-num 기법으로 하나 재끼고 하나만 찾는 방식
    - two pointer 기법: 시작점, 끝점 정해놓고 조건에 따라 시작+1 or 끝-1 하는 방식
    
https://leetcode.com/problems/two-sum/
https://leetcode.com/problems/trapping-rain-water/
https://leetcode.com/problems/3sum/)
https://leetcode.com/problems/array-partition/
https://leetcode.com/problems/product-of-array-except-self/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
https://leetcode.com/problems/kth-largest-element-in-an-array    
'''
import re
from typing import List

#     - Q1. (Easy) Leetcode 1. Two Sum: (https://leetcode.com/problems/two-sum/)
#     - 풀이: we can do brute force, but it will take O(n^2) time complexity. 
#     - therefore, we use target-num vs nums_map strategy
#     - two pointer method: always think of two pointer method for any array questions (for even three pointers)
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
            
        ### (add) what if two pointers?
        # left, right = 0, len(nums)-1
        
        # # need to have nums.sort()
        # if nums[left] + nums[right] < target:
        #     left += 1
        # elif nums[left] + nums[right] > target:
        #     right -= 1
        # else:
        #     return [left, right]
        

#     - Q2. (Hard) Leetcode 42. Trapping Rain Water: (https://leetcode.com/problems/trapping-rain-water/)
#     - 풀이:  two pointers, make sure that you assign left, right, left_max, right_max and move left/right pointers by given condition
class Solution:
    def trap(self, height: List[int]) -> int:
        # this is an exception code, where height doesn't exist 
        if len(height) < 2:
            return 0

        # using two pointer method, that is assign start, end points as left and right
        # also, assing left_max, and right_max to calulate max length of each pointers
        volume = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]

        # iterate until left and right meets
        while left < right:
            # update max length of each left and right pointers
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])          

            # after update, if left max is less or equal to right max, add left_max - current left 
            # this makes sense as right(or left) max length will be a bar for water to get trapped 
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
                
        # return the accumulated result
        return volume
    
    
#     - Q3. (Medium) Leetcode 15. 3Sum: (https://leetcode.com/problems/3sum/)
#     - 풀이:  iterate i and use two pointers
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        # this makes -4, -1, -1, 0, 1, 2
        nums.sort()

        # iterate from i 
        for i in range(len(nums) - 2):
            # as we've sorted, we don't want the same value to be used 
            # so, skip for the same value
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # assign two pointers which is start+1, and end
            #  so we check if i + left + right == 0
            left = i+1
            right = len(nums)-1

            # iterate until left meets right 
            while left < right:

                # get sum 
                sums = nums[i] + nums[left] + nums[right]

                # if sum is less than 0, it means that left pointer should move forward 
                if sums < 0:
                    left += 1
                # if sum is larger than 0, it means that right pointer should move backward 
                elif sums > 0:
                    right -= 1
                # else, append the result, and move left/right pointers at once 
                # this makes sense as result is already met, so both pointers should move 
                # also, if there are same values, move once more to avoid duplicates 
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    
                    # avoid duplicates
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    # move pointers    
                    left += 1                        
                    right -= 1
                    
        # return final result             
        return results 
                    
                    
#     - Q4. (Easy) Leetcode 561. Array Partition: (https://leetcode.com/problems/array-partition/)
#     - 풀이:  just think this as a sorting problem and adding index from 0 to the end by moving 2 indexes         
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        # to get maxmimum sum of mins, we can just sort and make pairs
        # so, we sort the list, and add all pairs by just looking at 0, 2, 4 th index of the list 
        return sum(sorted(nums)[::2])
    
    

#     - Q5. (Medium) Leetcode 238. Product of Array Except Self: (https://leetcode.com/problems/product-of-array-except-self/)
#     - 풀이: think as left multiples times right multiples 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create multiples from left and right
        # and multiply left by right each
        # we also put a placeholder for each end for left/right 
        res = []

        # left
        p = 1
        for i in range(len(nums)):
            res.append(p)
            p *= nums[i]
        
        # right, this is to rearrange index from max len to zero
        p = 1
        for i in range(len(nums) -1, 0 -1, -1):
            res[i] *= p
            p *= nums[i]
        
        return res    
    
    
#     - Q6. (Easy) Leetcode 121. Best Time to Buy and Sell Stock: (https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
#     - 풀이: assign min price and proft, then update by iterating time period    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initialize profit = 0, in case it was not updated 
        profit = 0
        min_price = sys.maxsize     

        # iterate price to update min_price, and also the profit
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        # return profit
        return profit

##### Additional questions        
#     - (Medium) Leetcode 215. Kth Largest Element in an Array: (https://leetcode.com/problems/kth-largest-element-in-an-array)
#     - 풀이: sorted, indexing 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # case1: using heapq
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n)

        for _ in range(k-1):
            heapq.heappop(heap)

        return -heapq.heappop(heap)        
        
        # case2: you sort the array, and take k-1 index (make sure you reversed)
        return sorted(nums, reverse=True)[k-1]    


