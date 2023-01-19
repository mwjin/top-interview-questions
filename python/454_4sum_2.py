from typing import List
from collections import defaultdict


class Solution:
    def fourSumCount(
        self,
        nums1: List[int],
        nums2: List[int],
        nums3: List[int],
        nums4: List[int],
    ) -> int:
        sum_dict1 = self.getSums(nums1, nums2)
        sum_dict2 = self.getSums(nums3, nums4)

        result = 0
        for n, cnt in sum_dict2.items():
            result += cnt * sum_dict1[-n]

        return result

    def getSums(self, nums1: List[int], nums2: List[int]) -> dict:
        result = defaultdict(int)
        for n1 in nums1:
            for n2 in nums2:
                result[n1 + n2] += 1
        return result
