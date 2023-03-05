'''
1. String
- 무기: 
    - 정규식(regular expression) 으로 불필요 문자 필터링: re.sub(‘[^a-z0-9]’, ‘’, s)
    - Reverse: str -> s[::-1], list -> s.reverse()
    - s.isdigit() : 숫자/문자 구분하기
    - Lambda 활용1(sort): letter_list.sort(key=lambda x: (x.split()[1:], x.split()[0])) 
    - List comprehension 사용, collections.defaultdict(int) 활용, dict의 argmax = max(dict, key=dict.get)
    - Slicing window 기법: create a function and iterate from i=0
    
https://leetcode.com/problems/valid-palindrome/
https://leetcode.com/problems/reverse-string/
https://leetcode.com/problems/reorder-data-in-log-files/
https://leetcode.com/problems/most-common-word/
https://leetcode.com/problems/group-anagrams/
https://leetcode.com/problems/longest-palindromic-substring/    
'''
import re
from typing import List

#     - Q1. (Easy) Leetcode 125. Valid Palindrome (https://leetcode.com/problems/valid-palindrome/)
#     - 풀이: 문제 설명 따라가면 되는데 re.sub 과 s[::-1] 뒤집기 항상 숙지하고 있기
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # after converting all uppercase letters into lowercase letters 
        s = s.lower()
        
        # removing all non-alphanumeric characters
        s = re.sub('[^a-z0-9]', '', s)

        # it reads the same forward and backward. 
        return s == s[::-1]


    # - Q2. (Easy) Leetcode 344. Reverse String: (https://leetcode.com/problems/reverse-string/)
    # - 풀이: 리스트는 .reverse() 로 뒤집자 
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # use reverse function provided by list class in python
        s.reverse()
       

    # - Q3. (Medium) Leetcode 937. Reorder Data in Log Files: https://leetcode.com/problems/reorder-data-in-log-files/)
    # - 풀이: split()해서 isdigit() 확인하는거랑, lambda function 잘 숙지하자  
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # we divide list into letter and digit lists 
        # initialize letter/digit lists
        letter_list, digit_list = [], []

        # for each string, check 1st index of each string and append to either letter or digit list
        for log in logs:
            if log.split()[1].isdigit():
                digit_list.append(log)
            else:
                letter_list.append(log)

        # The letter-logs are sorted lexicographically by their contents.
        # If their contents are the same, then sort them lexicographically by their identifiers.
        # The digit-logs maintain their relative ordering.
        letter_list.sort(key=lambda x: (x.split()[1:], x.split()[0]))     

        # Return the final order of the logs.
        # The letter-logs come before all digit-logs.
        return letter_list + digit_list


    # - Q4. (Easy) 819. Most Common Word: (https://leetcode.com/problems/most-common-word/)
    # - 풀이: using list comprehension + get used to defaultdict + and use max(dict, key=dict.get) as argmax 
import re
import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # # first remove all non alphanumeric words and convert all words into lowercase
        # # then, filter out banned word 
        words = [word for word in re.sub('[^a-z0-9]', ' ', paragraph.lower()).split() if word not in banned]
        
        ## method 1
        # # use collections library to find (word, word_cnt) pairs 
        # counts = collections.Counter(words)

        # # return most common word, by using most_common function 
        # # this creates [[word, count]], so need to index [0] twice 
        # return counts.most_common(1)[0][0]

        ## method 2
        # define defaultdict, which is more flexible than dict 
        # as this can append new key by just adding 
        counts = collections.defaultdict(int)

        # this creates {word: cnt} pair 
        for word in words: 
            counts[word] += 1
        
        # this works similarly as argmax
        # that is, you use counts.get to get the value of each key 
        # and this can be used to return keys that have maximum value 
        return max(counts, key=counts.get)


    # - Q5. (Medium) 49. Group Anagrams: (https://leetcode.com/problems/group-anagrams/)
    # - 풀이: use defaultdict(list), and used sorted(word) as a key, and append word as a value 
    # - Then, use .values for the defaultdict to get values (+list() makes computation time more faster)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # create a defaultdict that contains list as a value 
        anagrams = collections.defaultdict(list)
        
        # iterate each word and append words by using sorted word
        # this makes grouped anagrams list by sorted word
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        # we only want its values, so return its values from defaultdict
        # also make sure to make it as a list 
        return list(anagrams.values())
    
    
    # - Q6. (Medium) 5. Longest Palindromic Substring: (https://leetcode.com/problems/longest-palindromic-substring/)
    # - 풀이: get used to slicing window method, for both odd and even pointers      
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # create a function that expands if there is a palindrome 
        # as we update left-1, we return left+1, and return right, as slicing already excludes right end 
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1 : right]

        # exception, if len is lower than 2, or entire string is same as reversed string
        # return entire string
        if len(s) < 2 or s == s[::-1]: 
            return s
    
        # this is normal logic 
        # initialize result
        result = ''

        # run slicing window for both odd and even counts 
        # update maximum length of result string
        for i in range(len(s) - 1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)
        
        return result
    
    
