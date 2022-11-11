import math


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = -1 if numerator ^ denominator < 0 else 1
        numerator, denominator = abs(numerator), abs(denominator)
        gcd = math.gcd(numerator, denominator)
        numerator //= gcd
        denominator //= gcd

        quotient = numerator // denominator
        numerator %= denominator

        if numerator == 0:
            return f"{sign * quotient}"

        return f"{'-' if sign < 0 else ''}{quotient}.{self.getDecimal(numerator, denominator)}"

    def getDecimal(self, numerator: int, denominator: int) -> str:
        decimalDigits = []
        remainToIdx = {}
        recurringIdx = -1
        idx = 0

        while numerator and recurringIdx == -1:
            numerator *= 10
            decimalDigits.append(str(numerator // denominator))
            numerator %= denominator

            if numerator in remainToIdx:
                recurringIdx = remainToIdx[numerator] + 1
            else:
                remainToIdx[numerator] = idx
                idx += 1

        if recurringIdx != -1:
            decimalDigits.insert(recurringIdx, "(")
            decimalDigits.append(")")

        return "".join(decimalDigits)
