from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = localMax = localMin = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                localMax, localMin = localMin, localMax
            localMax = max(nums[i], localMax * nums[i])
            localMin = min(nums[i], localMin * nums[i])
            result = max(result, localMax)

        return result


print(Solution().maxProduct([0, 2]))
print(Solution().maxProduct([2, 3, -2]))
print(Solution().maxProduct([2, 3, -2, 4, 5]))
print(Solution().maxProduct([2, -5, -2, -4, 3]))
