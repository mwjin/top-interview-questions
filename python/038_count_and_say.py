class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            return convertDigitStr(self.countAndSay(n - 1))


def convertDigitStr(digitStr: str) -> str:
    currDigit = digitStr[0]
    digitCnt = 1
    cntResults = []

    for i in range(1, len(digitStr)):
        if digitStr[i] == currDigit:
            digitCnt += 1
        else:
            cntResults.append((digitCnt, currDigit))
            currDigit = digitStr[i]
            digitCnt = 1

    cntResults.append((digitCnt, currDigit))
    return "".join(map(lambda result: f"{result[0]}{result[1]}", cntResults))


print(convertDigitStr("3322251"))
print(Solution().countAndSay(4))
