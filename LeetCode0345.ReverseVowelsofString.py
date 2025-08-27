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


"""
Q: Given a string s, reverse only all the vowels in the string and return it.
I re-solve this question again by use diffrent approach to make it use less time complexity
1. Create set of vowels incliude vowels in Upper and Lower case.
2. Use the same loop logic to loop until first < last
3. Create 2 more loop to move index first and last depends on whether it in vowels or not
4. Then swap when everything in place

Runtime
7
ms
Beats
89.42%

Memory
18.46
MB
Beats
91.25%

"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)
        first, last = 0, len(s) - 1

        while first < last:
            while first < last and s[first] not in vowels:
                first += 1
            while first < last and s[last] not in vowels:
                last -= 1
            s[first], s[last] = s[last], s[first]
            first += 1
            last -= 1

        return "".join(s)

