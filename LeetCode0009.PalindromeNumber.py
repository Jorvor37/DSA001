"""
Q: Find is the given number is Palindrome or not, Palindrome number is the number that can read from left to right and right to left which hold the same value like 121
I solve this question by 
1. Convert integer into string to comapre string
2. Split the given number in half
3. Check whether first number and last number are the same or not then move them inwards to the middle
4. if spot it's not replicate(same number) we return False. This is not palindrome number or else otherwise
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_string = str(x)
        size = len(x_string)
        
        for i in range(size // 2):
            if x_string[i] != x_string[size - i - 1]:
                return False
        return True
