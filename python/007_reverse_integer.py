class Solution:
    max_val = 2 ** 31

    def reverse(self, x: int) -> int:
        result = 0
        is_negative = x < 0
        x = abs(x)

        while x > 0:
            result *= 10
            result += x % 10
            x //= 10

        if is_negative:
            result *= -1

        return result if -self.max_val <= result <= self.max_val - 1 else 0
