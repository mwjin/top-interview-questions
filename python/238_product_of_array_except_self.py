from typing import List
from functools import reduce


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = list(nums)
        for i in range(1, len(nums)):
            result[i] *= result[i - 1]

        cumulative = 1
        result[-1] = result[-2]
        for i in range(len(nums) - 2, 0, -1):
            cumulative *= nums[i + 1]
            result[i] = result[i - 1] * cumulative
        result[0] = cumulative * nums[1]

        return result


print(Solution().productExceptSelf([1, 2, 3, 4]))
print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))
