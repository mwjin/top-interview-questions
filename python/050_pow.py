class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        abs_n = abs(n)

        while abs_n > 0:
            temp = x
            p = 2

            while p <= abs_n:
                temp *= temp
                p *= 2

            result *= temp
            abs_n -= p // 2

        if n < 0:
            result = 1 / result

        return result


Solution().myPow(2, 10)
