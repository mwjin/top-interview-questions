from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        idx = reach = 0

        while idx < len(nums) and idx <= reach:
            reach = max(idx + nums[idx], reach)
            idx += 1

        return idx == len(nums)


print(Solution().canJump([2, 3, 1, 1, 4]))
print(Solution().canJump([3, 2, 1, 0, 4]))
