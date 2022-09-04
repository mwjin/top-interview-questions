from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        if not nums:
            return result

        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        if nums[left] != target:
            return result

        result[0] = left
        right = len(nums) - 1

        while left < right:
            mid = right - (right - left) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1

        result[1] = right if nums[right] == target else result[0]
        return result


print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
