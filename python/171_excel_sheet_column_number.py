class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0

        for alpha in columnTitle:
            result *= 26
            result += ord(alpha) - ord("A") + 1

        return result
