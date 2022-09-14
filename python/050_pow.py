class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n *= -1

        return (
            self.myPow(x * x, n // 2)
            if n % 2 == 0
            else x * self.myPow(x * x, n // 2)
        )


Solution().myPow(2, 10)
