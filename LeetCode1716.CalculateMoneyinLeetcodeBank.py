class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n//7
        #w1 = 28, w2 = 35, w3 = 42 each week is $7 more than the initial
        temp = 28
        total = 0
        for i in range (0, weeks):
            total += temp
            temp += 7
        day_left = n % 7
        n = weeks + 1
        temp = 0
        for i in range (0, day_left):
            temp += n
            n += 1
        return total + temp
