from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)

        for i, ch in enumerate(shortest):
            for otherStr in strs:
                if otherStr[i] != ch:
                    return shortest[:i]

        return shortest


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
