from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lsearch(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            result = -1

            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    result = mid
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1

            return result

        def rsearch(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            result = -1

            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    result = mid
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return result

        return [lsearch(nums, target), rsearch(nums, target)]


print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
