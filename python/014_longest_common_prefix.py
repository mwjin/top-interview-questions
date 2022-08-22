from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefixIdx = -1
        common = True

        while common:
            prefixIdx += 1

            for s in strs:
                if prefixIdx >= len(s) or s[prefixIdx] != strs[0][prefixIdx]:
                    common = False
                    break

        return strs[0][:prefixIdx]


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
