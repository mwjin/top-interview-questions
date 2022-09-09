from typing import List


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        matchTable = initMatchTable(s, p)
        for i, sCh in enumerate(s):
            for j, pCh in enumerate(p):
                if sCh == pCh or pCh == "?":
                    matchTable[i + 1][j + 1] = matchTable[i][j]
                elif pCh == "*":
                    matchTable[i + 1][j + 1] = (
                        matchTable[i][j + 1]
                        or matchTable[i][j]
                        or matchTable[i + 1][j]
                    )
        return matchTable[len(s)][len(p)]


def initMatchTable(s: str, p: str) -> List[List[bool]]:
    result = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
    result[0][0] = True

    for i in range(len(p)):
        if p[i] == "*":
            result[0][i + 1] = result[0][i]

    return result


print(Solution().isMatch("cb", "?a"))
