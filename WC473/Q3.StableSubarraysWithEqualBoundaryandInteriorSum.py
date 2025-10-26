from typing import List
from collections import defaultdict

class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        n = len(capacity)
        if n < 3:
            return 0

        # prefix[i] = sum of capacity[0..i-1]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + capacity[i]

        # counts of (capacity[r], prefix[r]) for r >= 2 (eligible r)
        counts = defaultdict(int)
        for r in range(2, n):
            counts[(capacity[r], prefix[r])] += 1

        ans = 0
        # iterate l from 0 to n-3 (so at least one r >= l+2 exists)
        for l in range(0, n - 2):
            target_prefix = capacity[l] + prefix[l+1]
            ans += counts.get((capacity[l], target_prefix), 0)

            # remove r = l+2 from counts because when l increments,
            # r must be >= (l+1)+2 = l+3
            r_to_remove = l + 2
            counts[(capacity[r_to_remove], prefix[r_to_remove])] -= 1
            if counts[(capacity[r_to_remove], prefix[r_to_remove])] == 0:
                del counts[(capacity[r_to_remove], prefix[r_to_remove])]

        return ans
©leetcode
