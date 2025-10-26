class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i: int, j: int) -> bool:
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                result = i == len(s)
            else:
                first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')
                if j + 1 < len(p) and p[j + 1] == '*':
                    # Use '*' as zero occurrence or move ahead in string if first matches
                    result = dp(i, j + 2) or (first_match and dp(i + 1, j))
                else:
                    result = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = result
            return result

        return dp(0, 0)
