from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(path=[]):
            if len(path) == len(nums):
                result.append(path)
                return

            for n in nums:
                if n not in path:
                    new_path = [*path, n]
                    dfs(new_path)

        dfs()
        return result


print(Solution().permute([1, 2, 3]))
print(Solution().permute([1, 2, 3, 4]))
