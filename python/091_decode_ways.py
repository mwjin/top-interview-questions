class Solution:
    def numDecodings(self, s: str) -> int:
        prevPrev = -1
        prev = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                curr = 0
            else:
                curr = prev
                if i < len(s) - 1 and int(s[i : i + 2]) <= 26:
                    curr += prevPrev
            prevPrev, prev = prev, curr

        return curr
