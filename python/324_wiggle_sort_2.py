from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums) // 2
        if len(nums) % 2 == 1:
            half += 1

        left, right = nums[:half], nums[half:]

        for i in range(0, len(nums), 2):
            nums[i] = left[-(i // 2) - 1]

        for i in range(1, len(nums), 2):
            nums[i] = right[-(i // 2) - 1]

        print(nums)


print(Solution().wiggleSort([1, 1, 2, 1, 2, 2, 1]))
print(Solution().wiggleSort([4, 5, 5, 6]))
