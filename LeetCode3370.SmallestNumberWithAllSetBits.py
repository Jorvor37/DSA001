class Solution:
    def smallestNumber(self, n: int) -> int:
        #1, 3, 7, 15
        List = []
        i = 0
        k = n
        while True:
            if k in List:
                return k
            elif k > ((2**i) - 1):
                i += 1
                List.append((2**i) - 1)
            else:
                k += 1
