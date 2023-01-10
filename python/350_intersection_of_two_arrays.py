from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        nums1_counter = Counter(nums1)

        result = []

        for n in nums2:
            if nums1_counter.get(n, 0) > 0:
                result.append(n)
                nums1_counter[n] -= 1

        return result
