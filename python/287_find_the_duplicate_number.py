from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        memory = set()
        for n in nums:
            if n in memory:
                return n
            memory.add(n)
