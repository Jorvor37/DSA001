from collections import Counter
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        freq1 = Counter(nums1)
        freq2 = Counter(nums2)
        common = set(freq1.keys()) & set(freq2.keys())
        for key in common:
            del freq1[key]
            del freq2[key]
        return [list(freq1.keys()), list(freq2.keys())]
