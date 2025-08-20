"""
Q: How to convert number in roman format into integer format
At first I solve this question by using the comcept of switch case from Java and C++
but after some research that cannot use in python I changed to use simple compare case instead which is pretty similar
1. Create set of values that which text belongs to which integer
2. We use loop to goes throguh each character
3. If position i+1 is exist and value in position i less than value at position i+1 we can lay it down due to these:
    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
    and then we skip two position as string in i and i+1 are used up so we don't use the string twice.
4. else it just regular string that exist we just skip 1 position as that what we used
5. We sum them up using one holding int array named "total"

"""
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        n = len(s)
        total = 0
        i = 0
        
        while i < n:
            if i+1 < n and values[s[i]] < values[s[i+1]]:
                total += values[s[i+1]] - values[s[i]]
                i += 2
            else:
                total += values[s[i]]
                i+=1
        return total
