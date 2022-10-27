import itertools
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(set(itertools.permutations(nums)))


print(Solution().permute([1, 1, 2]))
