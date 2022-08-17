import re


class Solution:
    def myAtoi(self, s: str) -> int:
        intPattern = re.search(r"^[+-]?\d+", s.lstrip())

        if not intPattern:
            return 0

        result = int(intPattern.group())
        if result < -(2 ** 31):
            result = -(2 ** 31)
        elif result >= 2 ** 31:
            result = 2 ** 31 - 1

        return result


print(Solution().myAtoi(" . hello 123 "))
print(Solution().myAtoi("    -123  hello"))
