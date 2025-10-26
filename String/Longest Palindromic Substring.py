class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s

        start, end = 0, 0

        for i in range(len(s)):
            len1 = self.expand_from_center(s, i, i)      # Odd-length palindrome
            len2 = self.expand_from_center(s, i, i + 1)  # Even-length palindrome
            max_len = max(len1, len2)

            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

    def expand_from_center(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # Length of the palindrome
