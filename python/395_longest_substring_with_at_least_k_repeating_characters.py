from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        counter = Counter(s)
        for c in counter:
            if counter[c] < k:
                return max(
                    self.longestSubstring(substr, k) for substr in s.split(c)
                )

        return len(s)
