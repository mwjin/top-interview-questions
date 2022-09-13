from typing import List
from collections import Counter, defaultdict


class Anagram:
    def __init__(self, s):
        self._counter = Counter(s)

    def __str__(self):
        return "".join(
            [f"{item[0]}{item[1]}" for item in sorted(self._counter.items())]
        )


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            result[str(Anagram(s))].append(s)

        return list(result.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
