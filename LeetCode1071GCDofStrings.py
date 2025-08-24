"""
Q: We are looking for the Greatest Common Divisor of two strings, which for convenience we will consider as the GCD string.
I cannot solve this problem on my own, so I did look up the Editorial part of the question and be able to understand it more then I comes up with this code
1. Check whether the two string have repeated value or not, if not return ""
2. Then focus on is there are divisible string or not by get gcdlength
3. Lastly we return prefix string in the lenght of either str1 or 2
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        length = gcd(len(str1), len(str2))
        return str1[:length]
