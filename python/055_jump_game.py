from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_idx = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= last_idx - i:
                last_idx = i

        return last_idx == 0


print(Solution().canJump([2, 3, 1, 1, 4]))
print(Solution().canJump([3, 2, 1, 0, 4]))
