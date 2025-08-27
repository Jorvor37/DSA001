"""
Q: Reverse Words in a String
I tackle this problem using new function I searched up called split(), it's make things 10 times easier
1. Let s = s.split() this function split string into words based on spacebar.
2. After we have array of words we reverse them inside for loop and we only do half size of words.
3. Return array word that join together by 1 spacebar with join function.

Runtime
0
ms
Beats
100.00%

Memory
17.86
MB
Beats
68.90%
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        size = len(s)
        for i in range (0, size//2):
            s[i], s[size-1] = s[size-1], s[i]
            size -= 1
        return " ".join(s)
