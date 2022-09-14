from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        localSum = nums[0]

        for i in range(1, len(nums)):
            localSum = max(localSum, 0) + nums[i]
            result = max(result, localSum)

        return result


print(Solution().maxSubArray([-1, -2, -3, -4, -5]))
