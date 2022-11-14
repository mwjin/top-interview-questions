import math


class Solution:
    def trailingZeroes(self, n: int) -> int:
        factorial = math.factorial(n)
        result = 0

        while factorial % 10 == 0:
            result += 1
            factorial //= 10

        return result
