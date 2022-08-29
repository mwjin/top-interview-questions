from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def pushParenthesis(path=[], numLeft=0, numRight=0):
            if numLeft == numRight == n:
                result.append("".join(path))
                return

            if numLeft < n:
                path.append("(")
                pushParenthesis(path, numLeft + 1, numRight)
                path.pop()

            if numRight < numLeft:
                path.append(")")
                pushParenthesis(path, numLeft, numRight + 1)
                path.pop()

        pushParenthesis()
        return result


print(Solution().generateParenthesis(3))
print(Solution().generateParenthesis(1))
