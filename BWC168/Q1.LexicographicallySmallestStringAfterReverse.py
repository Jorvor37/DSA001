class Solution:
    def lexSmallest(self, s: str) -> str:
        n = len(s)
        smallest = s
        for k in range(1, n + 1):
            # Build reversed prefix/suffix once
            prefix_rev = s[:k][::-1]
            suffix_rev = s[-k:][::-1]
            smallest = min(
                smallest,
                prefix_rev + s[k:],
                s[:-k] + suffix_rev
            )
        return smallest
