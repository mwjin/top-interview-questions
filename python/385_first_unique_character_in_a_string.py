from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        charCounter = Counter(s)

        result = 0
        while result < len(s) and charCounter[s[result]] != 1:
            result += 1

        return -1 if result == len(s) else result
