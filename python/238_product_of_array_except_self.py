from typing import List
from functools import reduce


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cumulative = list(nums)
        for i in range(1, len(nums)):
            cumulative[i] *= cumulative[i - 1]

        cumulativeRev = list(nums)
        for i in range(len(nums) - 2, -1, -1):
            cumulativeRev[i] *= cumulativeRev[i + 1]

        result = [cumulativeRev[1]]
        for i in range(1, len(nums) - 1):
            result.append(cumulative[i - 1] * cumulativeRev[i + 1])
        result.append(cumulative[-2])
        return result


print(Solution().productExceptSelf([1, 2, 3, 4]))
print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))
