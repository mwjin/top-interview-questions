from collections import Counter
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = Counter(nums)
        offset = 0

        for n in range(3):
            for i in range(offset, offset + cnt[n]):
                nums[i] = n
            offset += cnt[n]


Solution().sortColors([2, 0, 2, 1, 1, 0])
