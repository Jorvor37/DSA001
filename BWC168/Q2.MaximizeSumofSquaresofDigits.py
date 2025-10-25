class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        temp = []
        rs = sum # remaining_sum
        for i in range(num):
            d = min(9, rs)
            temp.append(d)
            rs -= d
        if rs != 0:
            return ""
        return "".join(map(str, temp))
©leetcode
