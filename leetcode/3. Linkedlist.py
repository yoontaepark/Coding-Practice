'''
3. LinkedList 
- 무기: 
    - self.val, self.next 항상 구도 생각하기
    - deque 개념: list + popleft and popright is done by O(1)
    - 2번 문제가 종합세트니 이거는 항상 풀고 코테들어가기
'''
import re
from typing import List, Optional

#     - Q1. (Easy) Leetcode 234. Palindrome Linked List: (https://leetcode.com/problems/palindrome-linked-list/)
#     - 풀이: deque - same as list but can use popleft, also compare by pop(0) or popleft() vs pop()

import collections

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # # case 1: create a list and compare by pop(0) and pop()
        # # create a list 
        # q = []

        # case 2: create a deque instead: deque can use popleft()
        q = collections.deque()

        # # exception: if there is nothing, retrun True
        if not head:
            return True
        
        # # iterate head and append its value
        while head is not None:
            q.append(head.val)
            head = head.next
        
        # # now, compare until length is more than 1
        # # and check if pop(0) and pop() is equal (this changes original value so we can iterate)
        while len(q) > 1:
        #     if q.pop(0) != q.pop():
            if q.popleft() != q.pop():
                return False
        
        # # return True, if all tests pass
        return True


#     - Q2. (Easy) Leetcode 21. Merge Two Sorted Lists: (https://leetcode.com/problems/merge-two-sorted-lists/)
#     - 풀이: deque - recursive function to compare both values and switch main list to smaller one 
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # we assign val - next pair so that we can sort two lists
        # if list1 is empty or list2 is not empty and list1's val is larger than list2's val, switch l1 and l2
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1

        # if list1 is not empty, assign list1.next as recursive function
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        
        return list1        


#     - Q3. (Easy) Leetcode 206. Reverse Linked List: (https://leetcode.com/problems/reverse-linked-list/)
#     - 풀이: recursive or iterate, either way requires a new empty list that replaces orignial list.next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # case1: recursive function
        # def reverse(node: Optional[ListNode], prev: Optional[ListNode] = None):
            
        #     # exit loop: if there is no more node, return prev and end recursive function
        #     if not node:
        #         return prev

        #     # assign node.next to next_, so that we can have [1:] of origin list
        #     # also, replace original node[1:] to prev so that we can update node to new one 
        #     # note that prev will be returned afterall 
        #     next_, node.next = node.next, prev

        #     # this is a recursive function, 
        #     return reverse(next_, node)

        # return reverse(head)
        
        # case2: iterate function
        # assign node and prev, prev will be returned afterall 
        node, prev = head, None

        # iterate until node is empty
        # assign next_ as node.next so that it contains node's next
        # and replace node.next to prev. this makes node to save value and None as node.next
        # iterate until node.val is None
        while node:
            next_, node.next = node.next ,prev
            prev, node = node, next_
        
        # after all, we will have a new list starting from end value (so it is reversed)
        return prev


#     - Q4. (M) Leetcode 2. Add Two Numbers: (https://leetcode.com/problems/add-two-numbers/)
#     - 풀이: we use almost everything we've learned in this linkedlist chapter

class Solution:
    # this is a reverse linked list function
    def reverseNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None
        while node:
            next_, node.next = node.next, prev
            prev, node = node, next_
        return prev

    # convert linked list to list
    def toList(self, node: Optional[ListNode]) -> List:
        res_list = []
        while node:
            res_list.append(node.val)
            node = node.next
        return res_list

    # convert string to reversed linked list 
    def toRevLinkedList(self, res: str) -> Optional[ListNode]:
        prev = None
        for r in res:
            node = ListNode(r)
            node.next = prev
            prev = node
        return prev

    # add two lists (main function)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # we reverse nodes and convert to list
        a = self.toList(self.reverseNode(l1))
        b = self.toList(self.reverseNode(l2))
        
        # then add two lists. we convert each integers to string and join, then convert back to integer
        # this is to have given digit number and add both integers 
        res = int(''.join(str(x) for x in a)) + int(''.join(str(y) for y in b))

        # then, we convert the value to reversed linked list 
        return self.toRevLinkedList(str(res))


#     - Q5. (M) Leetcode 24. Swap Nodes in Pairs: (https://leetcode.com/problems/swap-nodes-in-pairs/)
#     - 풀이: think this as a recursive function problem 
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if pair exists, do below
        if head and head.next:
            # we will return p, so firstly assign next to current to switch next and current 
            p = head.next

            # for original node, we use recursive function to iterate further nodes
            head.next = self.swapPairs(p.next)

            # assign head to p.next so that we assign reversed pair
            p.next = head

            # return final reversed pair
            return p

        # exit code for recursive function 
        return head


#     - Q6. (M) Leetcode 328. Odd Even Linked List: (https://leetcode.com/problems/odd-even-linked-list/)
#     - 풀이: assigned head is updated by .next 
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # exception
        if head is None:
            return head
        
        # initialize as odd and even, even_head will be used to attach odd.next
        odd = head
        even = head.next
        even_head = head.next

        # we iterate until even and even.next exists
        # as node starts from odd, it would be wise to loop on even, as none.next will make an error
        while even and even.next:
            # for both odd and even, we replace .next to .next.next
            # also, replace odd/even to .next 
            # head is updated when odd.next is updated
            odd.next = odd.next.next
            even.next = even.next.next 
            odd = odd.next 
            even = even.next
            
        # assign even list to end of odd 
        odd.next = even_head
        
        # return final head 
        return head
 

#     - Q7. (M) Leetcode 92. Reverse Linked List II: (https://leetcode.com/problems/reverse-linked-list-ii/)
#     - 풀이: make sure you understand linking logic 
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # exception
        if not head or left == right:
            return head

        # this makes both root and start start with None and next = head 
        root = start = ListNode(None)
        root.next = head
        
        # we move starting point to left-1, so that we can reverse from left 
        # end point is next of starting point, as we are reversing from right to left 
        # start/end point will be fixed, and other nodes will be updated 
        for _ in range(left-1):
            start = start.next
        end = start.next

        # now change node for right-left times 
        # i.e. [1,2,3,4,5]
        # tmp = 2 / 3,4,5, start = 1 / 3,4,5, end = 2 / 4,5
        # tmp is also updated as 2 / 4,5
        for _ in range(right-left):
            tmp = start.next
            start.next = end.next
            end.next = end.next.next

            # we move tmp to next.next so that we can reverse list 
            # this makes 1 / 3 / 2 / 4,5
            start.next.next = tmp

        return root.next
        
            
        
