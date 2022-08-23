from collections import defaultdict
from email.policy import default
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sortedNums = sorted(nums)

        for i in range(len(sortedNums) - 2):
            if i > 0 and sortedNums[i - 1] == sortedNums[i]:
                continue

            left = i + 1
            right = len(sortedNums) - 1

            while left < right:
                total = sortedNums[i] + sortedNums[left] + sortedNums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append(
                        [sortedNums[i], sortedNums[left], sortedNums[right]]
                    )
                    while (
                        left < right
                        and sortedNums[left] == sortedNums[left + 1]
                    ):
                        left += 1
                    while (
                        left < right
                        and sortedNums[right] == sortedNums[right - 1]
                    ):
                        right -= 1
                    left += 1
                    right -= 1

        return result


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
print(Solution().threeSum([0, 0, 0, 0]))
