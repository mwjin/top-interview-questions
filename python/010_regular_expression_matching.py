class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True

        for j, pChar in enumerate(p, 1):
            if pChar == "*":
                dp[0][j] = dp[0][j - 2]

        for i, sChar in enumerate(s, 1):
            for j, pChar in enumerate(p, 1):
                if sChar == pChar or pChar == ".":
                    dp[i][j] = dp[i - 1][j - 1]
                elif pChar == "*":
                    prevChar = p[j - 2]
                    if prevChar == sChar or prevChar == ".":
                        dp[i][j] = dp[i][j - 1] or dp[i][j - 2] or dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 2]

        return dp[len(s)][len(p)]


print(Solution().isMatch("aab", "c*a*b"))
print(Solution().isMatch("mississippi", "mis*is*ip*."))
