from typing import List

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        def simulate(start: int, direction: int) -> bool:
            arr = nums[:]  # copy to avoid mutation
            n = len(arr)
            curr = start

            while 0 <= curr < n:
                if arr[curr] == 0:
                    curr += direction 
                else:
                    arr[curr] -= 1
                    direction *= -1  # reverse
                    curr += direction

            return all(x == 0 for x in arr)

        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if simulate(i, 1):  # right
                    count += 1
                if simulate(i, -1):  # left
                    count += 1
        return count
