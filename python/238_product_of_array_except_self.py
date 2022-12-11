from typing import List
from functools import reduce


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in range(len(nums))]

        m = 1
        for i in range(len(nums)):
            result[i] *= m
            m *= nums[i]

        m = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= m
            m *= nums[i]

        return result


print(Solution().productExceptSelf([1, 2, 3, 4]))
print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))
