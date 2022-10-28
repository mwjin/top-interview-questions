from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memory = {}

        def helper(s: str) -> bool:
            if not s:
                return True
            if s in memory:
                return memory[s]

            for word in wordDict:
                if word == s[: len(word)] and helper(s[len(word) :]):
                    memory[s] = True
                    return True

            memory[s] = False
            return False

        return helper(s)


print(Solution().wordBreak("a", ["b"]))
