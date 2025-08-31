"""
Q: Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Runtime
0
ms
Beats
100.00%

Memory
18.84
MB
Beats
49.27%
"""
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero], nums[i] = nums[i], nums[non_zero]
                non_zero += 1
