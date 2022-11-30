from typing import List
from random import choice


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(nums: List[int], k: int) -> int:
            if len(nums) == 1:
                return nums[0]

            pivot = choice(nums)
            greater = []
            equal = []
            less = []

            for n in nums:
                if n > pivot:
                    greater.append(n)
                elif n == pivot:
                    equal.append(n)
                else:
                    less.append(n)

            if len(greater) >= k:
                return quickSelect(greater, k)
            elif len(greater) + len(equal) >= k:
                return pivot
            else:
                return quickSelect(less, k - len(greater) - len(equal))

        return quickSelect(nums, k)
