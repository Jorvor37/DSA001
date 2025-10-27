class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        total = 0
        for row in bank:
            c1 = row.count('1')
            if c1 > 0:
                total += prev * c1
                prev = c1
        return total
