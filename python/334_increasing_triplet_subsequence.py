from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        s = m = l = nums[0]

        for n in nums:
            if m != l and l < n:
                return True

            if n < s:
                s = n
            elif s < n and (n < l or m == l):
                m = s
                l = n

        return False
