# 과제4.
# 2개의 단어 beginWord와 endWord, 그리고 여러개의 단어 wordList가 주어졌을 때, beginWord에서 endWord로 변환하기 위해 필요한 가장 적은 변환 횟수를 구하시오.

# 변환 조건
# 단어는 wordList에 있는 단어로만 변환할 수 있다.
# 단어를 변환할 때에는 한번에 하나씩의 문자만 바꿀 수 있다.
# 문제 조건

# endWord로의 변환이 불가한 경우에는 0을 출력하시오.
# 문제에 등장하는 모든 단어의 길이는 같으며, 알파벳 소문자로만 이루어져 있다.
# wordList에는 겹치는 단어가 없다.
# beginWord와 endWord는 같은 단어로 주어지지 않는다.

# 예시 입력1
# 입력:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"] 
# 출력: 5 
# 설명: 가장 짧은 변환 방법은 "hit" -> "hot" -> "dot" -> "dog" -> "cog"이다.

# 예시 입력2
# 입력:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"] 
# 출력: 0 
# 설명: endWord인 "cog"가 wordList에 없으므로, endWord로 변환할 수 있는 방법이 없다.

def solution(beginWord, endWord, wordList):
    
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    if endWord not in wordList: return 0

    q = [(beginWord, 1)]
    while q:
        word, length = q.pop(0)
        if word == endWord:
            return length
        
        for i in range(len(word)):
            for char in alphabet:
                trans = word[:i] + char + word[i+1:]
                if trans in wordList:
                    wordList.remove(trans)
                    q.append((trans, length+1))
                    print(q)


# Case 1
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"] 
print(solution(beginWord, endWord, wordList))

# Case 2
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"] 
print(solution(beginWord, endWord, wordList))