#sceond attempt(better)
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain.insert(0, 0)
        for i in range(1, len(gain)):
            gain[i] = gain[i-1]+gain[i]
        return max(gain)

#first attempt
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = []
        altitudes.append(0)
        for i in range(len(gain)):
            altitudes.append(altitudes[i] + gain[i])
        return max(altitudes)
