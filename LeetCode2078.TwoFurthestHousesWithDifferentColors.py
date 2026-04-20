class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        first = 0
        last = len(colors)-1
        while(True):
            if colors[first] != colors[len(colors)-1]:
                return (len(colors)-1)-first
            elif colors[last] != colors[0]:
                return last - 0
            else:
                first += 1
                last -= 1
