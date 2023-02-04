'''
11. greedy algo
- 무기: 
    - 쪼갤수 있으면 그리디 알고리즘, 아니면 다이나믹 프로그래밍
    - 이진트리가 정렬되어 있지 않은 경우, 다른쪽 트리에 필요한 값을 못가겨자면 그리디 x
'''
import re
from typing import List, Optional
import collections

# 122. Best Time to Buy and Sell Stock II: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # initialize the profit
        profit = 0
        
        # iterate every index to find any next index that is bigger than current index
        for day in range(len(prices)-1):
            # if next index is larger, then buy current index price and sell at next index price 
            if prices[day+1] > prices[day]:
                # add all results and after iteration,
                profit += prices[day+1] - prices[day]
                
        # return the final result
        return profit


# 406. Queue Reconstruction by Height: https://leetcode.com/problems/queue-reconstruction-by-height/description/
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # idea: use priority que (max heap) to order each lists 

        # put all elements in heap
        # make sure to add negative [0] as we want max heap 
        heap = []
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))

        # now pop each heap and insert element by given index
        # note that you have to (-) back, as we pushed by negative [0]
        res = []
        while heap:
            person = heapq.heappop(heap)
            res.insert(person[1], [-person[0], person[1]])

        # return final result
        return res
    

# 621. Task Scheduler: https://leetcode.com/problems/task-scheduler/description/
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # idea: use collections.Counter and iterate each most_common keys until n
        # will iterating we add count, and at the end of iteration, we also add idle count
        # return final count

        # define collections.Counter
        counter = collections.Counter(tasks)
        cnt = 0

        # now iterate until counts gets empty
        while True: 
            # initialize sub count. This will be used to count idle
            sub_cnt = 0

            # now iterate each keys and count. also, remove counts
            # we set n+1, in case we don't have to add idle for n+1 cases 
            for task, _ in counter.most_common(n+1):
                sub_cnt += 1
                cnt += 1

                # remove counts that are counted
                counter.subtract(task)

                # this removes all items that have value = 0 or less than 0 
                counter += collections.Counter()

            # break loop 
            if not counter:
                break
            
            # adding idle
            cnt += n+1 - sub_cnt

        # now return final result 
        return cnt
    
    
# 134. Gas Station: https://leetcode.com/problems/gas-station/description/    
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # check if total gas is enough to travel all points
        if sum(gas) < sum(cost):
            return -1

        # now, iterate to check unique starting point 
        # there should have one answer 
        start, fuel = 0, 0
        for i in range(len(gas)):

            # given i point can't travel, so move to another starting point 
            if gas[i] + fuel < cost[i]:
                start = i+1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
            
        # return final starting point             
        return start
    
# 455. Assign Cookies: https://leetcode.com/problems/assign-cookies/description/
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # sort children / cookies
        g.sort()
        s.sort()
        child_i, cookie_j = 0, 0

        # compare each child-cookie pair and count
        while child_i < len(g) and cookie_j < len(s):
            # if cookie is larger than child, then child is filled and move
            if g[child_i] <= s[cookie_j]:
                child_i += 1
            # if not, that means we are moving to the next cookie
            cookie_j += 1

        # return satisfied child
        return child_i


# 169. Majority Element: https://leetcode.com/problems/majority-element/description/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 1) you can use collections.Counter, most_common as majority element is unique
        return collections.Counter(nums).most_common(1)[0][0]

        # 2) or you can sort array and point out exact middle index 
        # return sorted(nums)[len(nums) // 2]
        
# 241. Different Ways to Add Parentheses: https://leetcode.com/problems/different-ways-to-add-parentheses/description/
# divide and conquer         
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # idea: divide by operators and compute 

        # compute function, takes left, right, and operator to calculate formula
        def compute(left, right, operator):
            res = []
            for l in left:
                for r in right:
                    # using eval function to calculate any operators
                    res.append(eval(str(l)+operator+str(r))) 
            return res

        # exit code for single digit string
        if expression.isdigit():
            return [int(expression)]

        # main function
        res = []
        for idx, val in enumerate(expression):
            if val in '+-*': #operators: +,-,*
                left = self.diffWaysToCompute(expression[:idx])
                right = self.diffWaysToCompute(expression[idx+1:]) # idx = operator

                # compute left, right, and operator. Using extend to make it non-nested list 
                res.extend(compute(left, right, val))

        return res
        
        
# 509. Fibonacci Number: https://leetcode.com/problems/fibonacci-number/description/        
# dynamic programming: using top-down(recursion), or bottom-up(iteration)        
class Solution:
    # assign a dictionary
    dp = collections.defaultdict(int)
    
    def fib(self, n: int) -> int:
        # ## case 1): Memoization(top-down)
        # # if n<=1, return n
        # if n<=1:
        #     return n

        # # if dp[n] is filled, return dp[n]
        # if self.dp[n]: 
        #     return self.dp[n]

        # # main function: add n-1, n-2 to get n
        # self.dp[n] = self.fib(n-1) + self.fib(n-2)

        # # return final dp[n]
        # return self.dp[n]


        ## case 2): Tabulation(bottom-up)
        self.dp[1] = 1
        for i in range(2, n+1):
            self.dp[i] = self.dp[i-1] + self.dp[i-2] #dp[0]=0, as we are using defaultdict 
        return self.dp[n]


# 53. Maximum Subarray: https://leetcode.com/problems/maximum-subarray/description/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # update every end index by adding previous one
        # we pile up the result into every index so that we can return the max value
        # if prev is less then zero, we can ignore it as zero
        for i in range(1, len(nums)):
            nums[i] += nums[i-1] if nums[i-1]>0 else 0
            print(nums)
        
        return max(nums)
    
    
# 70. Climbing Stairs: https://leetcode.com/problems/climbing-stairs/description/
class Solution:
    # define dynamic programming dict 
    dp = collections.defaultdict(int)
    def climbStairs(self, n: int) -> int:
        # this can be interpreted as fibonacci
        # initial setup: if n<=2, return n itself
        if n<=2:
            return n

        # for intermediate result, return df[n]
        if self.dp[n]:
            return self.dp[n]
        
        # main function, we add up n-1 + n-2
        self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)

        # return final result
        return self.dp[n]
    
    
# 198. House Robber: https://leetcode.com/problems/house-robber/description/    
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <=2:
            return max(nums)
        
        dp = collections.OrderedDict() # this is a way to create an ordered dict (however, defaultdict also works)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            print(dp)
            
        # or you can do return list(dp.values())[-1]
        return dp.popitem()[1] # for dictionary, popitem pops the last index    
        
    