from typing import Counter, List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        numCnt = Counter(nums)

        def dfs(path=[]):
            if len(path) == len(nums):
                result.append(list(path))
                return

            for n in numCnt.keys():
                if numCnt[n] > 0:
                    path.append(n)
                    numCnt[n] -= 1
                    dfs(path)
                    path.pop()
                    numCnt[n] += 1

        dfs()
        return result


print(Solution().permuteUnique([1, 1, 2]))
