from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []

        def dfs(s: str, path: List[str] = []):
            if not s:
                result.append(" ".join(path))
                return

            for word in wordDict:
                if word == s[: len(word)]:
                    substr = s[len(word) :]
                    path.append(word)
                    dfs(substr, path)
                    path.pop()

        dfs(s)
        return result


print(Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
