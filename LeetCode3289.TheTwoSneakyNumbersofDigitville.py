class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = {}
        answer = []
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
            if seen[num] == 2:
                answer.append(num)
                if len(answer) == 2:
                    return answer
        else:
            print("No number appears twice.")
