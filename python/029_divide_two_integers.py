class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def trim_result(result: int) -> int:
            int_min = -(2 ** 31)
            int_max = 2 ** 31 - 1
            return (
                min(result, int_max) if result >= 0 else max(int_min, result)
            )

        if divisor == 1:
            return trim_result(dividend)
        if divisor == -1:
            return trim_result(-dividend)

        result = 0

        sign = 1 if dividend ^ divisor >= 0 else -1
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)

        while abs_dividend >= abs_divisor:
            q = 1
            temp_divisor = abs_divisor
            while temp_divisor < abs_dividend:
                temp_divisor <<= 1
                q <<= 1

            if temp_divisor > abs_dividend:
                temp_divisor >>= 1
                q >>= 1

            abs_dividend -= temp_divisor
            result += q

        return trim_result(result if sign == 1 else -result)
