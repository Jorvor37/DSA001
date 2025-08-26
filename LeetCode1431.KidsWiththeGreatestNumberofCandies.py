"""
Q: Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
I solve this problem by use simple if else statement in for loop\
1. Find the maximum value in candies array
2. If candies of i kid + extra candies is more than or equal we return True, else otherwise
3. We do that process for all number od kids
"""
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest_candies = max(candies)
        answer = []
        for i in range (0, len(candies)):
            if (candies[i] + extraCandies) >= greatest_candies:
                answer.append(True)
            else:
                answer.append(False)
        return answer
