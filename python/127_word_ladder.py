from collections import deque
from typing import List


class Solution:
    def ladderLength(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        def onlyOneDiff(word1: str, word2: str) -> bool:
            cnt = 0
            for c1, c2 in zip(word1, word2):
                cnt += c1 != c2
                if cnt > 1:
                    return False
            return True

        result = 1
        queue = deque([beginWord])
        visited = {beginWord}
        remain = set(wordList)

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return result

                for otherWord in remain:
                    if otherWord not in visited and onlyOneDiff(
                        word, otherWord
                    ):
                        queue.append(otherWord)
                        visited.add(otherWord)

            for word in queue:
                remain.remove(word)

            result += 1

        return 0


print(
    Solution().ladderLength(
        "red", "tax", ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]
    )
)
