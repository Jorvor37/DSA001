"""
Q: Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
Firstly I solve ethis problem in-correctly by using simple if else condition where if value at i < i+1 < i+2 return True, which is work for testcase but not covered all cases. So then I have to rethink and comes up with this method instead where we loop until we find all i, j, and k value we return True, return False for other cases
1. For loop through all numbers in nums.
2. Then check one by one if n less than equal to i_num, we find lowest number and continue
3. So now we have lowest i number then we do it again with j number, with this two we always have i as lowest amongs this trio and j as second lowest among this trio.
4. If we can find 3rd number that nomt rewrite the i or j, we now find the highest number among them.
"""

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i_num = j_num = float('inf')
        for n in nums:
            if n <= i_num:
                i_num = n
            elif n <= j_num:
                j_num = n
            else:
                return True
        return False
