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

