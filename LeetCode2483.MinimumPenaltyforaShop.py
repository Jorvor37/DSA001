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


#fixed version
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
