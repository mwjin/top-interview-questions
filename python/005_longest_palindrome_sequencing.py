from typing import Tuple


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getPalindromeIdx(start: int, end: int) -> Tuple[int, int]:
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            start += 1
            end -= 1
            return (start, end)

        maxStart = maxEnd = 0

        for i in range(len(s)):
            start, end = getPalindromeIdx(i - 1, i + 1)
            if (maxEnd - maxStart) < (end - start):
                maxStart, maxEnd = start, end

            start, end = getPalindromeIdx(i, i + 1)
            if (maxEnd - maxStart) < (end - start):
                maxStart, maxEnd = start, end

        return s[maxStart : maxEnd + 1]
