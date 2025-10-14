class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiouAEIOU")
        cur = sum(1 for ch in s[:k] if ch in vowels)
        max_vowel = cur

        for i in range(k, len(s)):
            if s[i] in vowels:
                cur += 1
            if s[i - k] in vowels:
                cur -= 1
            max_vowel = max(max_vowel, cur)

        return max_vowel
