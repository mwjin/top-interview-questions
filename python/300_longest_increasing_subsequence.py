from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = 1
        lis_lens = [1 for _ in range(len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            j = i + 1
            lis_len = lis_lens[i]
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    lis_len = max(lis_len, lis_lens[i] + lis_lens[j])
            lis_lens[i] = lis_len
            result = max(result, lis_lens[i])
        return result


print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]))
