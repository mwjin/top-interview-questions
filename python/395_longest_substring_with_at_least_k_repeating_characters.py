class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        charset = set(s)
        for c in charset:
            if s.count(c) < k:
                return max(
                    self.longestSubstring(substr, k) for substr in s.split(c)
                )

        return len(s)
