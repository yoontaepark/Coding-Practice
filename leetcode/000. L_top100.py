# top 100 questions in leetcode 

# 1. Two Sum: https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a reverse value: index dict and check the answer
        reversed_dict = collections.defaultdict(int)
        for i, num in enumerate(nums):
            reversed_dict[num] = i
        
        # then check to see if there is a match
        for i, num in enumerate(nums):
            if target-num in reversed_dict and i != reversed_dict[target-num]:
                return [i, reversed_dict[target-num]]
        

# 2. Add Two Numbers: https://leetcode.com/problems/add-two-numbers/description/
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # we can simply iterate to add one by one from left, but putting carry variable to add 1 or not
        # initialize dummy for a final result, and cur to move nodes, also set carry to add 1 or not in next digit
        dummy = cur = ListNode(0)
        carry = 0

        # iterate until all three variables are used
        while l1 or l2 or carry: 
            if l1: # add l1 val and move to next pointer 
                carry += l1.val
                l1 =l1.next 
            if l2: # add l2 val and move to next pointer 
                carry += l2.val
                l2 =l2.next 

            cur.next = ListNode(carry%10) # add remainder of carry to cur.next 
            cur = cur.next # move to next node

            # set carry to 1 or 0 for adding on the next digit
            carry //= 10

        # all set, return dummy.next to show the result 
        return dummy.next

# 3. Longest Substring Without Repeating Characters: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create a dict to save given index's word and use two pointers
        seen = {}
        max_length = 0
        start = 0

        # loop, idx is right pointer and start is left pointer
        for idx, char in enumerate(s):
            if char in seen and start <= seen[char]: # this means that we have to restart
                start = seen[char] + 1 # so move your starting pointer to one step right 
            else: 
                max_length = max(max_length, idx-start+1)

            # you always update your index, for given char
            seen[char] = idx

        return max_length
        
# 4. Median of Two Sorted Arrays: https://leetcode.com/problems/median-of-two-sorted-arrays/description/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # you extend array and sort
        nums1 = nums1 + nums2
        nums1.sort() # this will take O(n logn)
        
        mid = len(nums1)//2

        if len(nums1) % 2 != 0:
            return nums1[mid]
        else: 
            return (nums1[mid-1] + nums1[mid]) / 2      
        
# 5. Longest Palindromic Substring: https://leetcode.com/problems/longest-palindromic-substring/description/        
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        if len(s) < 2 or s==s[::-1]:
            return s

        result = ''
        for i in range(len(s)-1):
            result = max(result, expand(i,i+1), expand(i,i+2), key=len)

        return result        
    
# 7. Reverse Integer: https://leetcode.com/problems/reverse-integer/description/    
class Solution:
    def reverse(self, x: int) -> int:
        if str(x)[0] == '-':
            res = int(str(x)[0] + str(x)[1:][::-1])
            if res < -2**31:
                return 0
            else:
                return res

        else: 
            res = int(str(x)[::-1])
            if res > 2**31 - 1:
                return 0
            else:
                return res
            
# 8. String to Integer (atoi): https://leetcode.com/problems/string-to-integer-atoi/description/
class Solution:
    def myAtoi(self, s: str) -> int:
        # remove leading whitespace
        s = s.lstrip()
        
        # check for sign
        sign = 1
        if s and (s[0] == '+' or s[0] == '-'):
            if s[0] == '-':
                sign = -1
            s = s[1:]
        
        # convert digits
        result = 0
        for c in s:
            if not c.isdigit():
                break
            result = result * 10 + int(c)
        
        # apply sign and clamp to 32-bit range
        result *= sign
        result = max(min(result, 2**31-1), -2**31)
        
        return result
    
    
    
    
#### extra
# 658. Find K Closest Elements: https://leetcode.com/problems/find-k-closest-elements/description/
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k # right is the upper limit that left can go 
        while left < right: # unitl left gets to right 
            mid = (left + right) // 2 # you check the mid point

            # this makes three conditions at once
            # assuming x can be among below, if x is more closer to arr[mid+k], then move left to mid point
            # 1) x | arr[mid] | arr[mid+k], 2) arr[mid] | x | arr[mid+k], 3) arr[mid] | arr[mid+k] | x   
            if x - arr[mid] > arr[mid + k] - x: 
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k] # we return left to left+k

    