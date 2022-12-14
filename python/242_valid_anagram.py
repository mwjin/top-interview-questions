from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = defaultdict(int)
        for i in range(len(s)):
            counter[s[i]] += 1
            counter[t[i]] -= 1

        return not any(counter.values())
