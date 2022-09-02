from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        self.nums = nums
        start_idx = self.find_start_idx()
        end_idx = start_idx - 1
        if end_idx < 0:
            end_idx += len(nums)
        self.pivot = len(nums) - start_idx

        left = self.get_org_idx(start_idx)
        right = self.get_org_idx(end_idx)
        mid = self.get_pivot_idx((left + right) // 2)

        while left <= right and nums[mid] != target:
            if nums[mid] < target:
                left = self.get_org_idx(mid) + 1
            else:
                right = self.get_org_idx(mid) - 1
            mid = self.get_pivot_idx((left + right) // 2)

        return mid if nums[mid] == target else -1

    def find_start_idx(self):
        for i in range(1, len(self.nums)):
            if self.nums[i - 1] > self.nums[i]:
                return i
        return 0

    def get_pivot_idx(self, org_idx: int):
        result = org_idx - self.pivot
        if result < 0:
            result += len(self.nums)
        return result

    def get_org_idx(self, pivot_idx: int):
        return (pivot_idx + self.pivot) % len(self.nums)


print(Solution().search([1, 3], 1))
print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
print(Solution().search([4, 5, 6, 7, 0, 1, 2], 3))
