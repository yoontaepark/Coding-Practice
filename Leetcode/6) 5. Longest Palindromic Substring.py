# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
# Example 3:

# Input: s = "a"
# Output: "a"
# Example 4:

# Input: s = "ac"
# Output: "a"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters (lower-case and/or upper-case)



class Solution:
    def longestPalindrome(self, s: str) -> str:
        # make a function that checks and makes palindromic
        def expand(left:int, right:int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1            
            
            # i.e if left = 0 : true, then left = -1, so should add 1 
            # right gets +1 but since index starts from 0, it should be end by right
            return s[left+1:right]
        
        # make an exceptional case 
        if len(s) < 2 or s == s[::-1]:
            return s     
        
        # loop starting by index 0, compare palindromic function of 2 and 3, then return max result
        result = ''
        
        # to check every index combination
        for i in range(len(s)-1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)
            
        return result
            
            
