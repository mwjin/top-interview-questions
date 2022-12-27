from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def replaceSmallestAmongLarger(nums: List[int], alt: int) -> int:
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = low + (high - low) // 2

                if nums[mid] < alt:
                    low = mid + 1
                else:
                    high = mid - 1

            nums[low] = alt

        lis = [nums[0]]

        for i in range(1, len(nums)):
            if lis[-1] < nums[i]:
                lis.append(nums[i])
            else:
                replaceSmallestAmongLarger(lis, nums[i])

        return len(lis)


print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]))
print(Solution().lengthOfLIS([4, 10, 4, 3, 8, 9]))
