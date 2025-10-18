class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stripped_s = s.strip()
        words = stripped_s.split()
        last_word = words[-1]
        return len(last_word)
