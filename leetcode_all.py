# 125: palindrome
# 알파벳 소문자로 바꾸고, 알파벳/숫자 아닌애들 다 날린담에 앞뒤가 맞는지 점검
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # alphabets transfer
        s = s.lower()
        
        # recognize only chr + alphabet
        s = re.sub('[^a-z0-9]', '', s)
                   
        return s == s[::-1]


# 344. Reverse String, 리스트니까 뒤집기 사용
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]


# 937. Reorder Data in Log Files, 
# 일단 숫자 문자 나누고, 문자는 소트하는데 2번 소트해야 함, 그리고 문자 + 숫자로 리턴
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # divide to letter-logs and digit-logs
        letters, digits = [], []        
        
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        # sort letter-logs, if same, then use identifier
        letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))
        
        # add letter + digit
        return letters + digits
        

# 819. Most Common Word
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # delete except alphabet, change to lowercase, split, and del banned
        words = [word for word in re.sub(r'[^\w]', '  ', paragraph)
                .lower().split() if word not in banned]
        
        # use collections.Counter w most_common method
        # counts should be sth like [('ball', 2), ('hit', 1)...]
        counts = collections.Counter(words)
        
        # most_common 1 to return [(ball, 2], and [0][0] for ball
        return counts.most_common(1)[0][0]
        

# 49. Group Anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # create dictionary w key: sorted(word) / value: word
        
        # create defaultdict 
        anagrams = collections.defaultdict(list)

        # loop words to make key(sorted word): value(origin word)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
            
        return list(anagrams.values())


# 5. Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # exception: len < 2 or s == s[::-1] -> True
        if len(s) < 2 or s == s[::-1]: 
            return s
        
        # create palindrome checker w expandable option
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1 : right]
        
        # check max length for each palindrome
        result = ''
        for i in range(len(s)-1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)
        
        return result

## 막간 상식: 스택은 연결 리스트, 큐는 배열로

# 1. Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # create dic and change key, value by using enumerate
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i
        
        # if target - one number is in keys, 
        # and index i is not equal to the new dict value, 
        # return i and new dict value 
        for i, num in enumerate(nums):
            if target-num in nums_map.keys() and i != nums_map[target-num]:
                return [i, nums_map[target-num]]


# 15. 3Sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # create result list and sort nums
        result = []
        nums.sort()  
        
        # exception: if next i is same as previous one, it is duplicated, pass
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
        
            # make three pointers with i, left(i+1), right(len(nums)-1)
            left, right = i+1, len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                
                # move left if sum <0, right if sum>0, append if sum = 0
                if sum < 0: 
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # while next left/right numbers are same, move
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    # move left and right and repeat while statement
                    left += 1
                    right -= 1
        
        return result
                        

# 561. Array Partition I
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:        
        # sum of even index is maximum
        # sort nums
        nums.sort()
        
        # return sum of even indexes
        return sum(nums[::2])
        
                
# 238. Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # initialize
        out = []        
        
        # make left/right multiples for each index(excluding self)
        # left multiples for each
        p = 1
        for i in range(0, len(nums)):
            out.append(p)
            p *= nums[i]
        
        
        # multiply right to left
        p = 1
        for i in range(len(nums)-1, -1, -1):
            out[i] *= p
            p *= nums[i]
            
        return out


# 121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initialize profit = 0 and min_price to max
        profit = 0
        min_price = sys.maxsize
        
        # use loop to check min_price & max profit        
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price-min_price)
        
        return profit


# 234. Palindrome Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:   
        
        # Exception
        if not head:
            return True
        
        # change linked list to list to check palindrome
        # also, to use deque to decrease runtime
        q = collections.deque()
        
        node = head
        
        while node is not None:
            q.append(node.val)
            node = node.next
        
        # check palindrome
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
            
        return True
                

# 21. Merge Two Sorted Lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # if l1 x or l2 head is smaller, than change
        if not l1 or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        
        # fix l1 but change l1.next to use recursion
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        
        return l1


# 206. Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # use recursion
        def reverse(node, prev=None):
            # exception, recursion out
            if not node:
                return prev
            
            # move node -> prev by using next
            next, node.next = node.next, prev
            return reverse(next, node)
        
        return reverse(head)



# 2. Add Two Numbers: 순서대로 정의하면서 풀어라
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:      
    # linked list -> reverse linked list
    def reverseList(self, head):
        node, prev = head, None
            
        while node:
            next, node.next = node.next, prev
            prev, node = node, next            
            
        return prev
        
        # linked list -> python list 
    def toList(self, node):
        list = []
        while node:
            list.append(node.val)
            node = node.next
                
        return list
        
        
    # python list -> reversed linked list
    def toReversedLinkedList(self, result):
        prev = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
            
        return node       
        
        
        # add two linked list 
    def addTwoNumbers(self, l1, l2):
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))
            
        resultStr = int(''.join(str(e) for e in a)) + \
                    int(''.join(str(e) for e in b))
            
        return self.toReversedLinkedList(str(resultStr))       
        
        
        
