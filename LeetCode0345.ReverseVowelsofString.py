"""
Q: Given a string s, reverse only all the vowels in the string and return it.
I solve this problem with simple array run through
1. Create funtion to check wheather that character is vowel or not.
2. Create index of first and last so that we can runthrough from front and back to find vowels to swap.
3. Use basic if else statement that when we find first and last vowels we swap, if found one not the other we use elif and else to handle that.

Runtime
32
ms
Beats
7.83%

Memory
18.53
MB
Beats
67.63%

"""

class Solution:
    VOWELS = {"a", "e", "i", "o", "u"}
    def is_vowel(self, ch: str) -> bool:
        return ch.lower() in self.VOWELS

    def reverseVowels(self, s: str) -> str:
        s = list(s)
        first = 0
        last = len(s) - 1
        while first < last:
            if self.is_vowel(s[first]) and self.is_vowel(s[last]):
                s[first], s[last] = s[last], s[first]
                first += 1
                last -= 1
            elif self.is_vowel(s[first]):
                last -= 1
            else:
                first += 1
        return "".join(s)
