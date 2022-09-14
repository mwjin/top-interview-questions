from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        localSum = 0

        for n in nums:
            localSum += n
            result = max(result, localSum)
            localSum = max(localSum, 0)

        return result


print(Solution().maxSubArray([-1, -2, -3, -4, -5]))
