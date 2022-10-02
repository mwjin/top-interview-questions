from typing import List


class Solution:
    def merge(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m]
        temp_idx = nums2_idx = 0
        for i in range(len(nums1)):
            if temp_idx < m and nums2_idx < n:
                if temp[temp_idx] < nums2[nums2_idx]:
                    nums1[i] = temp[temp_idx]
                    temp_idx += 1
                else:
                    nums1[i] = nums2[nums2_idx]
                    nums2_idx += 1
            elif temp_idx < m:
                nums1[i] = temp[temp_idx]
                temp_idx += 1
            elif nums2_idx < n:
                nums1[i] = nums2[nums2_idx]
                nums2_idx += 1
