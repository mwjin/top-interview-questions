from collections import defaultdict
from email.policy import default
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sortedNums = sorted(nums)

        for i in range(len(sortedNums) - 2):
            if i > 0 and sortedNums[i - 1] == sortedNums[i]:
                continue

            total = -sortedNums[i]
            diffToIdx = {}
            diffCnt = defaultdict(int)

            for j in range(i + 1, len(sortedNums)):
                if sortedNums[j] in diffToIdx:
                    if diffCnt[sortedNums[j]] == 0:
                        diffCnt[sortedNums[j]] += 1
                        k = diffToIdx[sortedNums[j]]
                        result.append(
                            [sortedNums[i], sortedNums[k], sortedNums[j]]
                        )
                else:
                    diffToIdx[total - sortedNums[j]] = j

        return result


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
print(Solution().threeSum([0, 0, 0, 0]))
