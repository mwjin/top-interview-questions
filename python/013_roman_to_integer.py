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

        for i in range(len(s) - 1):
            if romanToIntMap[s[i]] < romanToIntMap[s[i + 1]]:
                result -= romanToIntMap[s[i]]
            else:
                result += romanToIntMap[s[i]]

        return result + romanToIntMap[s[-1]]
