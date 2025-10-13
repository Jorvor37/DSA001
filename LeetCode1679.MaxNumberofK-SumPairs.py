from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = Counter()
        ops = 0

        for num in nums:
            c = k - num
            if freq[c] > 0:
                freq[c] -= 1
                ops += 1
            else:
                freq[num] += 1
        return ops
