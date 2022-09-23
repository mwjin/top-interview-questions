from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        remain = len(t)

        minWindowStart, minWindowSize = 0, len(s) + 1

        start = 0
        for end in range(len(s)):
            if count[s[end]] > 0:
                remain -= 1
            count[s[end]] -= 1

            while remain == 0:
                currWindowSize = end - start + 1
                if minWindowSize > currWindowSize:
                    minWindowStart, minWindowSize = start, currWindowSize

                count[s[start]] += 1
                if count[s[start]] > 0:
                    remain += 1
                start += 1

        return (
            ""
            if minWindowSize == len(s) + 1
            else s[minWindowStart : minWindowStart + minWindowSize]
        )


print(Solution().minWindow("ADOBECODEBANC", "ABC"))
