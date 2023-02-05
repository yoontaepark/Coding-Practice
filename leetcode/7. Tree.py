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


# 617. Merge Two Binary Trees: https://leetcode.com/problems/merge-two-binary-trees/description/
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # idea: we simply add node values of each roots 
        # two cases: if both roots are available
        if root1 and root2:
            # merging happens here
            node = TreeNode(root1.val + root2.val)

            # for left and right, we run recursive function 
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)

            # return node as a final result 
            return node
        
        # if either is not None, then it will return not None
        # if both are None, return None
        else: 
            return root1 or root2
        

# 110. Balanced Binary Tree: https://leetcode.com/problems/balanced-binary-tree/description/
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # idea: put leaf nodes as 0, and add up to check root
        # if end of this function (=root) is -1, return Flase, else True
        def check(node):
            # to set up None nodes as 0
            if not node:
                return 0
            
            # set left, right to the leaf node 
            left = check(node.left)
            right = check(node.right)

            # we set not available nodes to -1, and we don't need to check n/a nodes and above
            # also, if |left-right| is larger than 1, it means that it is not balanced => -1
            if left == -1 or right == -1 or abs(left-right)>1:
                return -1
            
            # node should be updated +1 of either max value of left and right 
            return max(left, right) + 1

        
        # check if root is -1, and return the boolean value 
        return check(root) != -1
        

# 310. Minimum Height Trees: https://leetcode.com/problems/minimum-height-trees/description/        
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # idea: first, we should fill edges into a graph
        # then we remove nodes that are leaf, and repeat this until there remains 1 or 2 answers 
        # 2 answers may exist, as we can think of example 2, were [3,4] can be switched 

        # exception code:
        if n <= 1:
            return [0]

        # constructing a graph
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # first iteration of setting up leaf nodes
        # this iteration is needed as a first step
        leaves = []
        for i in range(n+1):
            if len(graph[i])==1:
                leaves.append(i)

        # below steps are repeated
        while n>2:
            # make sure to remove leaf nodes until n gets 2 or below 
            # also, create a temp new_leaves list
            n -= len(leaves)
            new_leaves = []
            # iterate each leaf node
            for leaf in leaves:
                # now, we pop leaf node's value. (which is parent node)
                neighbor = graph[leaf].pop()

                # from parent node, remove child node as well
                graph[neighbor].remove(leaf)

                # now check parent node to see if they can be leaf node
                # if so, append to the new_leaves list
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            
            # now, update new leaves into leaves 
            leaves = new_leaves
        
        # after all, return leaves 
        return leaves        


# 108. Convert Sorted Array to Binary Search Tree: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # idea: we get mid, and simply use recursive function for left, and right

        # exception, and exit loop
        if not nums:
            return None
        
        # get mid. Make sure you round down to get a correct index (we are using 0-indexing)
        mid = len(nums) // 2

        # create a node with val = mid index of nums
        node = TreeNode(nums[mid])
        
        # for left and right, use recursive function
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])

        # return node
        return node
    
    
# 1038. Binary Search Tree to Greater Sum Tree: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/
class Solution:
    # define a value that would be accumulated and updated 
    val = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # idea: you update the val of TreeNode, but start from right to left
        # if root, then repeat below
        if root: 
            self.bstToGst(root.right) # this makes root to the right end
            self.val += root.val # this updates the val 
            root.val = self.val # update what we want (value of root TreeNode)
            self.bstToGst(root.left) # now look up for left as well

        # return updated root
        return root    
        
        
# 938. Range Sum of BST: https://leetcode.com/problems/range-sum-of-bst/description/
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        # create a dfs and add values if val is in inclusive range (low, high)
        def dfs(node):
            if not node: return 0 # this is to convert values into 0 where conditions don't meet

            # also, add some truncate terms
            # if val < low, we truncate left cases. Same logic applies to the right cases
            if node.val < low: return dfs(node.right)
            elif node.val > high: return dfs(node.left)

            # we will be returning val, and recursively check left/right child node to add val 
            return node.val + dfs(node.left) + dfs(node.right)

        
        # run dfs and return its value
        return dfs(root)


                