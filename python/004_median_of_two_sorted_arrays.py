from typing import List


class Solution:
    MAX_VALUE = 1000001

    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        self.nums1 = nums1
        self.nums2 = nums2
        left = (len(nums1) + len(nums2) + 1) // 2
        right = (len(nums1) + len(nums2) + 2) // 2
        return (
            self.findKthElement(left, 0, 0) + self.findKthElement(right, 0, 0)
        ) / 2

    def findKthElement(self, k: int, nums1_offset: int, nums2_offset: int):
        if nums1_offset >= len(self.nums1):
            return self.nums2[nums2_offset + k - 1]
        if nums2_offset >= len(self.nums2):
            return self.nums1[nums1_offset + k - 1]
        if k == 1:
            return min(self.nums1[nums1_offset], self.nums2[nums2_offset])

        nums1_idx = nums1_offset + k // 2 - 1
        nums2_idx = nums2_offset + k // 2 - 1

        nums1_val = (
            self.nums1[nums1_idx]
            if nums1_idx < len(self.nums1)
            else self.MAX_VALUE
        )
        nums2_val = (
            self.nums2[nums2_idx]
            if nums2_idx < len(self.nums2)
            else self.MAX_VALUE
        )

        if nums1_val < nums2_val:
            return self.findKthElement(
                k - k // 2, nums1_offset + k // 2, nums2_offset
            )
        else:
            return self.findKthElement(
                k - k // 2, nums1_offset, nums2_offset + k // 2
            )
