class Solution:
    def climbStairs(self, n: int) -> int:
        result = prev = 1
        for _ in range(n - 1):
            result, prev = result + prev, result
        return result
