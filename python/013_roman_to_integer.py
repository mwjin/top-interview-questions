class Solution:
    def romanToInt(self, s: str) -> int:
        romanToIntMap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = 0
        prevNum = 10000

        for c in s:
            currNum = romanToIntMap[c]
            if prevNum < currNum:
                result -= 2 * prevNum
            result += currNum
            prevNum = currNum

        return result
