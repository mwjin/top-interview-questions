class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        divider = 5

        while n // divider != 0:
            result += n // divider
            divider *= 5

        return result
