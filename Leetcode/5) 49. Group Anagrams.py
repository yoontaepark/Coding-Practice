# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lower-case English letters.



# Solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # create a new defaultdict that starts with a default list value
        anagrams = collections.defaultdict(list)
        
        # to group anagrams, sort each word as a key and append as a value
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
            
        
        # return new grouped list of a value 
        return anagrams.values()
