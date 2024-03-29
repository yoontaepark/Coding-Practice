'''
6. Graph
- 무기: 
    - 개념적으로 아예 이해가 안될 건 아니니까 매일 다시 풀어보면서 암기를 하자
    - dfs 로 대부분 풀린다. (일단 dfs로 풀고 안되면 못푼다고 생각하자)
    - dfs의 다양한 유형들을 암기하고, 이것들을 유형화해서 추가추가하는 식으로 관리하자  
'''
import re
from typing import List, Optional
import collections

# - 문제
#     - (Medium) Leetcode 200. Number of Islands: (https://leetcode.com/problems/number-of-islands/)
#     - 풀이: nested function 으로 dfs 구현하는 기초문제 (이거는 꼭 암기하자)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != '1':
                return

            grid[i][j] = '0' # can convert this to any values except '1'

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i,j)
                    count += 1
        
        return count
    
    
#     - (Medium) Leetcode 17. Letter Combinations of a Phone Number: (https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
#     - 풀이: 같은 맥락인데(위와), 아래에 dfs 돌리고, 위에서 dfs 재귀 치는걸 유의할 것 
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        def dfs(index, path):
            # if length of path is same as digits, it means that letter combination is finished
            # therefore, append the result and exit
            if len(path) == len(digits):
                res.append(path)
                return

            # we pick digit[i]'s j value and add until i increases till digits 
            # path is then finalized and the result is saved at the exit code 
            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i+1, path+j)

        # exception
        if not digits:
            return []

        # manually assign dictionary
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        # initialize final result
        res = []

        # run dfs
        dfs(0, '')

        return res    


#     - (Medium) Leetcode 46. Permutations: (https://leetcode.com/problems/permutations)
#     - 풀이: nested dfs 같은 유형인데 리턴을 안받고 res.append를 하는 유형 (리턴해도 됨)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # case1: dfs
        # assign result list and prev list (which will save the result and append to the result list)
        res = []
        prev = []

        # main function
        def dfs(elements):
            # exit, if len == 0, append the result. note that we need to copy values only (not the references)
            if len(elements) == 0:
                res.append(prev[:]) # [:] copies only the value 
                return 

            # iterate and set up next_, and prev
            for e in elements:
                # for next_, we remove e from element list 
                next_ = elements[:]
                next_.remove(e)

                # for prev, we append e, run dfs(next), pop prev
                prev.append(e)
                dfs(next_) # this ends when next_ is empty, and we append prev(pop didn't happen yet)
                prev.pop()

        # we simply run dfs algorithm 
        dfs(nums)

        # return result list 
        return res    
    
        ### case2: itertools 
        # 이건 그냥 암기하자: itertools -> list(map(list, itertools.permutations(nums)))
        return list(map(list, itertools.permutations(nums)))    
    

#     - (Medium) Leetcode 77. Combinations: (https://leetcode.com/problems/combinations/)
#     - 풀이: nested dfs 같은 유형인데 리턴을 받음. range의 끝이 고정인 유형 
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # case1: dfs
        res = []

        def dfs(elements, start, end):
            # exit code, we append result and exit 
            if end == 0:
                res.append(elements[:])
                return
            
            # iteration for end is fixed, as we want to loop till the end 
            # but starting point should be changed
            for i in range(start, n+1):
                # add i to given element 
                elements.append(i)
                # we want to run this function recursively, but not i itself
                # also, we repeat until end = 0 (from so therefore, list is (k, k-1, ... 1), len(list) = k
                dfs(elements, i+1, end-1)
                # this is to remove end value and replace to next value
                elements.pop()

        # 1 is given as we need to choose numbers from the range (1, n)
        # k is the given condition, and we will decrease this to 0 (and this makes k numbers of combination)
        dfs([], 1, k)

        # return final result
        return res    
    
        ## case2: itertools
        return list(map(list, itertools.combinations(range(1, n+1), k)))
    
    
#     - (Medium) Leetcode 39. Combination Sum: (https://leetcode.com/problems/combination-sum/)
#     - 풀이: nested dfs의 또 다른 유형 (sum - candidate 하면서 반복하는 케이스 )
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()

        def dfs(csum, index, path):
            if csum < 0:
                return 
            if csum == 0:
                res.append(path[:])
                return 

            for i in range(index, len(candidates)):
                dfs(csum-candidates[i], i, path+[candidates[i]])

        dfs(target, 0, [])

        return res    
    
    
#     - (Medium) Leetcode 78. Subsets: (https://leetcode.com/problems/subsets/)
#     - 풀이: nested dfs, return 없는 케이스 
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(index, path):

            res.append(path)
            
            for i in range(index, len(nums)):
                dfs(i+1, path+[nums[i]])

        dfs(0, [])

        return res    
    

    # - (Medium) 332. Reconstruct Itinerary: (https://leetcode.com/problems/reconstruct-itinerary/)
    # - 풀이: create a grpah, dfs
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # create a graph
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)

        # making a route, this is a reversed route
        route = []
        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop(0))
            route.append(start)
        dfs('JFK')

        # filp route 
        return route[::-1]
    
    
    # - (Medium) 207. Course Schedule: (https://leetcode.com/problems/course-schedule)
    # - 풀이: create a grpah, dfs    
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # setup graph 
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        # check to see if graph is cyclic or not, by using dfs 
        # we create two sets, to check if it is traced / visited
        traced = set()
        visited = set()

        # dfs function
        def dfs(i):
            # first, check if it is in traced. if so, it means that our graph is cyclic so return False
            if i in traced:
                return False

            # if the node is visited, then return True and exit
            if i in visited:
                return True

            # add node into traced and continue tracing 
            traced.add(i)
            # for prerequisite of i, run dfs again and see if prerequisite is in traced. 
            for y in graph[i]:
                if not dfs(y):
                    return False

            # after checking, remove nodes from other sibling nodes 
            traced.remove(i)

            # after all, add i to visited 
            visited.add(i)

            # after all tests are done, return True
            return True

        # main function: just iterate to see if given course x passes dfs function 
        for x in list(graph):   
            if not dfs(x):
                return False
        
        # after all tracing has been succeed, return True
        return True
    
    
'''
6-2. Shortest Path 
- 무기: 
    - 개념적으로 아예 이해가 안될 건 아니니까 매일 다시 풀어보면서 암기를 하자 
'''
import re
from typing import List, Optional
import collections

# - 문제
#     - (Medium) Leetcode 743. Network Delay Time: (https://leetcode.com/problems/network-delay-time/)
#     - 풀이: 최단경로찾기) bfs (or 다익스트라) 구현한다고 생각하면서 접근 

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # creating a graph 
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w)) 

        # creating a queue that initialize as 0 for starting point k
        # also create an empty dict that will contain (node, distance from k) 
        Q = [(0, k)]
        dist = collections.defaultdict(int)
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
        
        # if dist has same length as n, it means that every node can get signal
        # then we return max value among other values
        if len(dist) == n:
            return max(dist.values())
        
        # if not, it means that not every node got signals, so return -1
        return -1


#     - (Medium) Leetcode 787. Cheapest Flights Within K Stops: (https://leetcode.com/problems/cheapest-flights-within-k-stops/)
#     - 풀이: 최단경로찾기) 다익스트라가 안됨(TLE), 안될경우의 대안을 생각해보기
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # create a dicttionary that contains value as a list
        # also, create a list of weight, so that we can truncate based on the weight condition
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v,w))

        weight = [(sys.maxsize, k)] * n

        # define path to destination
        Q = [(0, src, k)]

        # we will loop this and end when it meets destination
        while Q:
            # for each lowest price node 
            price, node, k = heapq.heappop(Q)
            
            # if node meets the destination, return the price
            # note that price would be the lowest price, as we are using heapq
            if node == dst:
                return price

            # until we use all stops, run below
            if k >= 0:
                # for each next nodes, add up price to get next node
                for v, w in graph[node]:
                    alt = price + w
                    # only update when price is lower than saved weight or we have more stops left 
                    if alt < weight[v][0] or k-1 >= weight[v][1]:
                        weight[v] = (alt, k-1) # update weight
                        heapq.heappush(Q, (alt, v, k-1)) # update new Q
        
        # if there is no such route, return -1
        return -1
        
    