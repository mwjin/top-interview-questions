from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if k == 0:
            return

        l = len(nums)
        offset = 0

        while k != 0:
            for i in range(k):
                nums[offset + i], nums[-k + i] = nums[-k + i], nums[offset + i]
            offset += k
            l -= k
            k %= l


Solution().rotate([6, 7, 1, 2, 3, 4, 5], 5)
Solution().rotate([8, 9, 10, 1, 2, 3, 4, 5, 6, 7], 7)
