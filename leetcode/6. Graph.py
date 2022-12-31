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