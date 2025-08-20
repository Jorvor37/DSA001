"""
Q: Find the two number in the list that sum to the target number, not allow to use the same number twice
I tackle this problem by using simple nested loop and if else condition
1. loop through all number if it's same position we skip
2. if it's not the same position(same number), we do if number at position i + number at postion j equals to target we return that two position
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range (0, n):
            for j in range (0, n):
                if(i!=j):
                    if(nums[i] + nums[j] == target):
                        return i, j
            #endfor
        #endfor
    
