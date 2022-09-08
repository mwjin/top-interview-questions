from collections import defaultdict, deque
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(path=[], visited=set()):
            if len(path) == len(nums):
                result.append(list(path))
                return

            for n in nums:
                if n not in visited:
                    visited.add(n)
                    path.append(n)
                    dfs(path, visited)
                    path.pop()
                    visited.remove(n)

        dfs()
        return result


print(Solution().permute([1, 2, 3]))
print(Solution().permute([1, 2, 3, 4]))
