import itertools


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            return convertDigitStr(self.countAndSay(n - 1))


def convertDigitStr(digitStr: str) -> str:
    group_length = lambda group: len(list(group))
    return "".join(
        [
            f"{group_length(group)}{digit}"
            for digit, group in itertools.groupby(digitStr)
        ]
    )


print(convertDigitStr("3322251"))
