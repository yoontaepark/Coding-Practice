'''
6. Graph
- 무기: 
    - 개념적으로 아예 이해가 안될 건 아니니까 매일 다시 풀어보면서 암기를 하자 
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
#            이건 그냥 암기하자: itertools -> list(map(list, itertools.permutations(nums)))
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