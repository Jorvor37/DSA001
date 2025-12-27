# time limit exceed version
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        final = []
        for i in range (0, len(customers)+1):
            penalty = customers[i:].count('Y')
            penalty += customers[:i].count('N')
            print("index" + str(i) + ":" + str(penalty))
            final.append(penalty)
        print(final)
        min_num = float('inf')
        min_index = 0
        for i in range (0, len(final)):
            if final[i] < min_num:
                min_num = final[i]
                min_index = i
        return min_index

"""
#fixed version
Runtime
611
ms
Beats
5.00%
Analyze Complexity
Memory
25.64
MB
Beats
14.20%
"""
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prefixN = [0] * (n + 1)
        suffixY = [0] * (n + 1)

        # prefix count of 'N'
        for i in range(n):
            prefixN[i + 1] = prefixN[i] + (customers[i] == 'N')
        # suffix count of 'Y'
        for i in range(n - 1, -1, -1):
            suffixY[i] = suffixY[i + 1] + (customers[i] == 'Y')

        min_penalty = float('inf')
        min_index = 0
        for i in range(n + 1):
            penalty = prefixN[i] + suffixY[i]
            print("index" + str(i) + ":" + str(penalty))
            if penalty < min_penalty:
                min_penalty = penalty
                min_index = i
        return min_index
"""
# Best version Runtime
47
ms
Beats
80.70%
Analyze Complexity
Memory
17.85
MB
Beats
98.10%
"""
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = customers.count('Y')  # initial close at 0
        min_penalty = penalty
        best = 0
        i = 0
        for c in customers:
            if c == 'Y':
                penalty -= 1
            else:
                penalty += 1
            i += 1
            if penalty < min_penalty:
                min_penalty = penalty
                best = i
        return best
