from math import sqrt


class Solution:
    memory = {}

    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        if n in self.memory:
            return self.memory[n]

        result = n
        for num in range(int(sqrt(n)), 0, -1):
            result = min(result, 1 + self.numSquares(n - num**2))
        self.memory[n] = result
        return result
