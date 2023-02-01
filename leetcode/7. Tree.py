'''
7. Tree
- 무기: 
    - TBD
'''
import re
from typing import List, Optional
import collections

# - 문제
# 104. Maximum Depth of Binary Tree: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # idea: define depth, and iterate to see any child nodes for each nodes
        if not root:
            return 0
        
        # define a deque that includes entire tree as a list 
        # also, define depth so that we can return depth as a result
        dequeue = collections.deque([root])
        depth = 0

        # if there is any node available at that stage, iterate 
        while dequeue:
            # depth + 1 if that stage is available 
            depth += 1

            # iterate each roots to add childs to dequeue
            for _ in range(len(dequeue)): 
                # popleft so that we can check from old ones
                cur_root = dequeue.popleft()
                # check if there are any left/right child and if so, append 
                if cur_root.left:
                    dequeue.append(cur_root.left)
                # same applies to right child 
                if cur_root.right:
                    dequeue.append(cur_root.right)

        # returning final result
        return depth            
