from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [100000 for _ in range(amount + 1)]
        dp[0] = 0

        for n in range(1, amount + 1):
            for c in coins:
                if n >= c:
                    dp[n] = min(dp[n], 1 + dp[n - c])

        return -1 if dp[amount] == 100000 else dp[amount]


print(Solution().coinChange([1, 2, 5], 11))
print(Solution().coinChange([2], 3))
print(Solution().coinChange([1], 0))
print(Solution().coinChange([1], 1))
