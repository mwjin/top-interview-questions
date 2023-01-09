from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_counter = Counter(nums1)
        nums2_counter = Counter(nums2)

        result = []

        for n in nums1_counter:
            count = min(nums1_counter[n], nums2_counter.get(n, 0))
            for _ in range(count):
                result.append(n)

        return result
