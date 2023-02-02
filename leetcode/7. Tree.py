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


# 543. Diameter of Binary Tree: https://leetcode.com/problems/diameter-of-binary-tree/description/
class Solution:
    # assign path count here, as we need to reallocate this integer in recursive function
    path_cnt = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # idea: update each node's depth from leaf node, and also update longest path
        # if left/right is available, we can add +2 to have longest path
        # if either left or right is not available, we assign -1 so that we can adjust the length of the path

        def dfs(node):
            # for unavailable nodes: -1
            if not node: return -1

            # recursive function to get leaf left / right 
            left = dfs(node.left)
            right = dfs(node.right)

            # update length of the path 
            self.path_cnt = max(self.path_cnt, left+right+2)

            # return depth of current node. should be +1 from its child node 
            return max(left, right) + 1

        # run dfs   
        dfs(root)

        # return total count 
        return self.path_cnt
    
    
# 687. Longest Univalue Path: https://leetcode.com/problems/longest-univalue-path/description/
class Solution:
    # set variable here, as it is handy to update result variable outside of the function
    res = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # idea: go to the leaf node, and start to calculate length of longest path
        # if value of node and node.left/right is different, reset length to 0

        # define dfs to search every possible length 
        def dfs(node):
            
            # if there is nothing, return 0
            if not node:
                return 0

            # left/right to the leaf node
            left = dfs(node.left)
            right = dfs(node.right)

            # now count from each left, right
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # update length
            self.res = max(self.res, left+right)

            # return either max of left or right 
            return max(left, right)


        # basically run dfs
        dfs(root)

        # return final result 
        return self.res
            
            
# 226. Invert Binary Tree: https://leetcode.com/problems/invert-binary-tree/description/
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if there is no root, return root itself
        if not root:
            return root

        # swap left/right
        root.left, root.right = root.right, root.left

        # run recursive function for both left/right 
        self.invertTree(root.left)
        self.invertTree(root.right)

        # return root
        return root

