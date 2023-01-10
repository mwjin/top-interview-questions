from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        nums1_idx = nums2_idx = 0

        result = []

        while nums1_idx < len(nums1) and nums2_idx < len(nums2):
            if nums1[nums1_idx] < nums2[nums2_idx]:
                nums1_idx += 1
            elif nums1[nums1_idx] > nums2[nums2_idx]:
                nums2_idx += 1
            else:
                result.append(nums1[nums1_idx])
                nums1_idx += 1
                nums2_idx += 1

        return result
