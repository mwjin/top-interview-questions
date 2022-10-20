from collections import deque
from typing import List


class Solution:
    def ladderLength(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        def wordGenerator(word) -> str:
            for i in range(len(word)):
                for c in range(ord("a"), ord("z") + 1):
                    yield word[:i] + chr(c) + word[i + 1 :]

        result = 1
        queue = deque([beginWord])
        words = set(wordList)

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return result
                for otherWord in wordGenerator(word):
                    if otherWord in words:
                        queue.append(otherWord)
                        words.remove(otherWord)

            result += 1

        return 0


print(
    Solution().ladderLength(
        "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
    )
)
