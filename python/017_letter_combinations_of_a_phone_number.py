from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToLetters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        if not digits:
            return []

        result = []

        def appendLetter(letters: List[str], digitIdx: int):
            if digitIdx == len(digits):
                result.append("".join(letters))
                return

            for letter in digitToLetters[digits[digitIdx]]:
                letters.append(letter)
                appendLetter(letters, digitIdx + 1)
                letters.pop()

        appendLetter([], 0)
        return result


print(Solution().letterCombinations(""))
