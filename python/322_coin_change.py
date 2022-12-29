from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memory = {}

        def dp(coins: List[int], amount: int) -> int:
            if amount in memory:
                return memory[amount]
            if amount < 0:
                return -1
            if amount == 0:
                return 0

            result = 100000

            for coin in coins:
                sub_result = dp(coins, amount - coin)
                if sub_result != -1:
                    result = min(result, 1 + sub_result)

            if result == 100000:
                result = -1

            memory[amount] = result
            return result

        return dp(coins, amount)


print(Solution().coinChange([1, 2, 5], 11))
print(Solution().coinChange([2], 3))
print(Solution().coinChange([1], 0))
print(Solution().coinChange([1], 1))
