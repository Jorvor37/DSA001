from collections import Counter

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        temp = n + 1
        while True:
            freq = Counter(str(temp))
            if all(freq[d] == int(d) for d in freq):
                return temp
            temp += 1
