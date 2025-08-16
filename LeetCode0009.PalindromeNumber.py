class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_string = str(x)
        size = len(x_string)
        
        for i in range(size // 2):
            if x_string[i] != x_string[size - i - 1]:
                return False
        return True
