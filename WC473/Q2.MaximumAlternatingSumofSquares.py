class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        #convert to all positive nums
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = -nums[i]

        nums.sort()
        n = int(len(nums)/2)
        
        return sum(x**2 for x in nums[n:]) - sum(x**2 for x in nums[:n])©leetcode
