"""
Q: Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

I solve this problem with simple logic, if both left and right is 0 we can plant
1. Create while loop that while flower(n) is not all planted and i is not the last position(size)
2. If flower at i position is 1 we skip by 2 then check again because at position i+1 cannot plant as of front position is 1
3. Else we use two variable, left and right empty to identify does it empty or not, prevent index out of range error by assign
4. If left and right empty we can plant so we set flowerbed[i] = 1 and n -= 1 and i += 2
5. Then we return True if all flower planted(n==0), else otherwise
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        size = len(flowerbed)

        while n > 0 and i < size:
            if flowerbed[i] == 1:
                i += 2
            else:
                left_empty = (i == 0) or (flowerbed[i-1] == 0)
                right_empty = (i == size-1) or (flowerbed[i+1] == 0)

                if left_empty and right_empty:
                    flowerbed[i] = 1
                    n -= 1
                    i += 2
                else:
                    i += 1

        if n == 0:
            return True
        else:
            return False
