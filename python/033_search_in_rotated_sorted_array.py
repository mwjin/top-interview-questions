from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        rotate = left
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            rotated_mid = (mid + rotate) % len(nums)
            if nums[rotated_mid] > target:
                right = mid - 1
            elif nums[rotated_mid] < target:
                left = mid + 1
            else:
                return rotated_mid

        return -1


print(Solution().search([1, 3], 0))
print(Solution().search([3, 1, 2], 0))
print(Solution().search([4, 2, 6, 7, 0, 1, 2], 0))
