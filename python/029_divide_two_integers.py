class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def trim_result(result: int) -> int:
            int_min = -(2 ** 31)
            int_max = 2 ** 31 - 1
            return max(min(result, int_max), int_min)

        if divisor == 1:
            return trim_result(dividend)
        if divisor == -1:
            return trim_result(-dividend)

        positive = (dividend < 0) == (divisor < 0)
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)

        result = 0

        while abs_dividend >= abs_divisor:
            q = 1
            temp_divisor = abs_divisor

            while abs_dividend >= temp_divisor:
                abs_dividend -= temp_divisor
                result += q
                temp_divisor <<= 1
                q <<= 1

        return trim_result(result if positive else -result)


print(Solution().divide(10, 3))
