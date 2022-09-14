class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        result = x
        p = 2
        abs_n = abs(n)

        while p <= abs_n:
            result *= result
            p *= 2

        result *= self.myPow(x, abs_n - p // 2)

        if n < 0:
            result = 1 / result

        return result


Solution().myPow(2, 10)
