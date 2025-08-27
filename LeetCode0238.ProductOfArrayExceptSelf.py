"""
Q: Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
I cannot solve this problem until I took a peak on hint1, therefore I follow
1. Pre-calculate products of nums before index i and after index i (prefix, suffix)
2. Multiply them together in answer array

Runtime
31
ms
Beats
33.03%

Memory
26.99
MB
Beats
19.36%
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pre = [1] * n
        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i-1]
        
        suff = [1] * n
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]
        
        ans = [0] * n
        for i in range(n):
            ans[i] = pre[i] * suff[i]
        
        return ans
