class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1 for _ in range(len(s) + 1)]
        dp[-1] = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
                if i < len(s) - 1 and int(s[i : i + 2]) <= 26:
                    dp[i] += dp[i + 2]

        return dp[0]
