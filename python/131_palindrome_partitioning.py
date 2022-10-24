from typing import List


class Solution:
    memory = {}

    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s: str):
            mid = len(s) // 2
            return s[:mid] == s[: -mid - 1 : -1]

        if len(s) == 0:
            return [[]]

        if len(s) == 1:
            return [[s]]

        if s in self.memory:
            return self.memory[s]

        result = []

        for i in range(1, len(s) + 1):
            left, right = s[:i], s[i:]
            if is_palindrome(left):
                for sub_partition in self.partition(right):
                    result.append([left, *sub_partition])

        self.memory[s] = result
        return result


print(Solution().partition("bb"))
