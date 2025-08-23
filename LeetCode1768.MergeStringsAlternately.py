"""
Q: You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Stat: 30ms beats 93.68% && 17.56MB beats 94.88%
I solve this problem by insert frist character one by one then delete the inserted one
1. Use while loop as if word1 and word2 is both exists we add them one by one
2. After that we append the left over whether it's word one or two
3. Return the join of the answer
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = []
        while word1 and word2:
            answer.append(word1[0])
            word1 = word1[1:]
            answer.append(word2[0])
            word2 = word2[1:]
        answer.append(word1)
        answer.append(word2)
        return "".join(answer)
