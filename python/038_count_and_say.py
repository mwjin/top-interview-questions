import itertools


class Solution:
    def countAndSay(self, n: int) -> str:
        digitStr = "1"

        for _ in range(n - 1):
            digitStr = convertDigitStr(digitStr)

        return digitStr


def convertDigitStr(digitStr: str) -> str:
    group_length = lambda group: len(list(group))
    return "".join(
        [
            f"{group_length(group)}{digit}"
            for digit, group in itertools.groupby(digitStr)
        ]
    )


print(convertDigitStr("3322251"))
print(Solution().countAndSay(4))
