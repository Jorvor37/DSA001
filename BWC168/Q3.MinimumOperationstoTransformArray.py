class Solution:
    def minOperations(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        base = 0
        for i in range(n):
            base += abs(nums1[i] - nums2[i])
        target = nums2[n]
        best_extra = float('inf')
        for k in range(n):
            a = nums1[k]
            b = nums2[k]
            lo, hi = (a, b) if a <= b else (b, a)
            if lo <= target <= hi:
                dist = 0
            else:
                dist = min(abs(target - lo), abs(target - hi))
            if dist < best_extra:
                best_extra = dist

        return base + 1 + best_extra
©leetcode
