from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        half = len(s) // 2
        for i in range(half):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
