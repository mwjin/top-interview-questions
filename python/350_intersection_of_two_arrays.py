from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_counter = Counter(nums1)
        nums2_counter = Counter(nums2)

        result = []

        if len(nums1_counter) < len(nums2_counter):
            small = nums1_counter
            large = nums2_counter
        else:
            small = nums2_counter
            large = nums1_counter

        for n in small:
            count = min(small[n], large.get(n, 0))
            for _ in range(count):
                result.append(n)

        return result
