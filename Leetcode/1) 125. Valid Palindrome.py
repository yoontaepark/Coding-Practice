#Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

#Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.


# Solution1: Change by list
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1) transfrom string into lower alphabet
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        # 2) check first-last index by using pop
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
            
        return True

# Solution2: Solution1 + using deque to increase performance
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1) transfrom string into lower alphabet
        strs: Deque = collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        # 2) check first-last index by using pop
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
            
        return True
  
# Solution3: Use slicing
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()        
        s = re.sub('[^a-z0-9]', '', s)        
        return s == s[::-1]
