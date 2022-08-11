from typing import List


class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        def merge(l1: List[int], l2: List[int]) -> List[int]:
            result = []
            i = j = 0

            while i < len(l1) and j < len(l2):
                if l1[i] < l2[j]:
                    result.append(l1[i])
                    i += 1
                else:
                    result.append(l2[j])
                    j += 1

            if i < len(l1):
                result += l1[i:]
            elif j < len(l2):
                result += l2[j:]
            return result

        def median(l: List[int]) -> float:
            mid = len(l) // 2
            return (
                float(l[mid]) if len(l) % 2 == 1 else (l[mid - 1] + l[mid]) / 2
            )

        return median(merge(nums1, nums2))
