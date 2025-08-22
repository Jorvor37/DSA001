"""
Q: Write a function to find the longest common prefix string amongst an array of strings.
I solve this problem useing neseted loop
1. Find the range that i and j needed to loop for
2. Check each index one by one compare with all strings in array
3. If found any mismatch return instant
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""

        shortest_string = strs[0]
        for s in strs:
            if len(s) < len(shortest_string):
                shortest_string = s


        for i in range (0, len(shortest_string)):
            for j in range (0, len(strs)):
                if strs[0][i] != strs[j][i]:
                    return answer
            answer = "".join([answer, strs[0][i]]) 
        return answer
