class Solution:
    def isValid(self, s: str) -> bool:
        pairParenthesisMap = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        stack = []

        for ch in s:
            if ch in pairParenthesisMap:
                if stack and pairParenthesisMap[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return not stack
