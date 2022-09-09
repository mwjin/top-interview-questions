class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sIdx = pIdx = sIdxMetWildcard = 0
        lastWildCard = -1

        while sIdx < len(s):
            if pIdx < len(p) and (s[sIdx] == p[pIdx] or p[pIdx] == "?"):
                sIdx += 1
                pIdx += 1
            elif pIdx < len(p) and p[pIdx] == "*":
                lastWildCard = pIdx
                sIdxMetWildcard = sIdx
                pIdx += 1
            elif lastWildCard != -1:
                pIdx = lastWildCard + 1
                sIdxMetWildcard += 1
                sIdx = sIdxMetWildcard
            else:
                return False

        while pIdx < len(p) and p[pIdx] == "*":
            pIdx += 1

        return pIdx == len(p)
