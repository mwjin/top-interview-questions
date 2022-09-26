from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(path: List[int] = [], start=0):
            result.append(path.copy())

            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(path, i + 1)
                path.pop()

        dfs()
        return result


print(Solution().subsets([1, 2, 3]))
