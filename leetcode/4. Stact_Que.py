'''
4. Stack, Que
- 무기: 
    - stack: LIFO, queue: FIFO, other than this we can use linkedlist and array to create each
    - we can also use deque to popleft or pop // also append in array(right append)
    - append and popleft append = left append 
    - circular: two pointers (front and rear)
'''
import re
from typing import List, Optional
import collections

# - 문제
#     - (Easy) Leetcode 20. Valid Parentheses: (https://leetcode.com/problems/valid-parentheses/)
#     - 풀이: create a reverse dict pair, and iterate symbol to either append or compare
#     - note that, even we set an elif function, it conducts .pop(), and stack is directly updated 

class Solution:
    def isValid(self, s: str) -> bool:
        # initialize stack list, and table 
        # we create a table in an opposite key-value pair
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        # iterate symbol, if symbol is not in table, append
        # if symbol is in table, check if stack is empty
        # elif: contains some exception cases, so if it starts from right (i.e. }, ), ]), then it is already wrong 
        # or if table value is not equal to pop, then it is wrong 
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False

        # we basically iterate and remove all pairs, so we need to check if len == 0
        # there can be cases where stack has only one value. then it is also false 
        return len(stack) == 0    
        
        
#     - (Medium) Leetcode 316. Remove Duplicate Letters: (https://leetcode.com/problems/remove-duplicate-letters/)
#     - 풀이: think of split point by using set 
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # we need to define char which can be seperated 
        # first we sort set of sentence, so that we can check by each char 
        for char in sorted(set(s)):

            # we assign suffix
            suffix = s[s.index(char):]

            # only when set of both sentence and suffix is equal, run recursive function
            if set(s) == set(suffix):
                # seperate char + recursive function
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        
        # if not exit as empty 
        return ''        
    

#     - (Medium) Leetcode 739. Daily Temperatures: (https://leetcode.com/problems/daily-temperatures/)
#     - 풀이: similar to q 121, think of always adding an index and pop(the last) when current temp is higher 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # if there is no update, return 0
        res = [0] * len(temperatures)
        stack = []

        # iterate for every temperatures
        for i, cur in enumerate(temperatures):
            # if there is a stack, and temperature of given stack is higher than current, 
            # then pop that and update the result 
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                res[last] = i - last
                
            # always append current index of temperature
            stack.append(i)
        
        # return final result
        return res    
    

#     - (Medium) Leetcode 225. Implement Stack using Queues: (https://leetcode.com/problems/implement-stack-using-queues/)
#     - 풀이: push algo, use popleft + append 
class MyStack:

    def __init__(self):
        # init function
        self.q = collections.deque()

    def push(self, x: int) -> None:
        # first append, this makes x to the end of the stack
        self.q.append(x)

        # then, loop to change the left front data to the end (right) of the stack
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        # removes the top element, this is be changed as self.q.pop(0)
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]
        
    def empty(self) -> bool:
        return len(self.q) == 0
    
    
#     - (Medium) Leetcode 232. Implement Queue using Stacks: (https://leetcode.com/problems/implement-queue-using-stacks/)
#     - 풀이: Using two lists, peek algo: fill q2 if q2 is empty until q1 gets empty
class MyQueue:

    def __init__(self):
        # using two stacks 
        self.q1 = collections.deque()
        self.q2 = collections.deque()        

    def push(self, x: int) -> None:
        self.q1.append(x)
        
    def pop(self) -> int:
        # create a reversed list from q1
        self.peek()
        # we then pop and also return popped data 
        return self.q2.pop()

    def peek(self) -> int:
        # create a reversed list(q2) from original list(q1)
        if not self.q2:
            while self.q1:
                self.q2.append(self.q1.pop())
        # this is to print out the first element from q1 
        return self.q2[-1]

    def empty(self) -> bool:
        return (len(self.q1)) == 0 and (len(self.q2) == 0)
    
    
#     - (Medium) Leetcode 622. Design Circular Queue: (https://leetcode.com/problems/design-circular-queue/)
#     - 풀이: update front/rear by using % total length 
class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0 # front
        self.p2 = 0 # end

    # p2 is rear, so append value and move one more (note that we need to divide into maxlen as it is a circular queue)
    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False

    # similar to enQueue, but using p1 
    def deQueue(self) -> bool:
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1] 

    # we defined enQueue to move p2 extra one step further, so we return p2 - 1
    def Rear(self) -> int:
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1] 

    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None
    
    

#     - (Hard) Leetcode 23. Merge k Sorted Lists: (https://leetcode.com/problems/merge-k-sorted-lists/)
#     - 풀이: should think of updating one variable when updates both but not updates the other 
import heapq
# priority queue -> heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode(None)
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            # pop, this pops out min value
            node = heapq.heappop(heap)
            
            # to save index(placeholder)
            idx = node[1]
            # this is to assign both root/result to its entire linked list
            # this assigns additional next for root 
            result.next = node[2]
            # this only updates the result, not the root
            result = result.next

            # updating next result 
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        # as root itself has no value, we return root.next
        return root.next

    