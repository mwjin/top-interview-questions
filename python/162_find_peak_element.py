from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while right - left > 1:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] <= nums[mid - 1]:
                right = mid - 1
            else:
                left = mid + 1

        if left == right:
            return left
        else:
            return left if nums[left] > nums[right] else right
