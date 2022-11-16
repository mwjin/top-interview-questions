from typing import List


class Number:
    def __init__(self, num: int):
        self._num = str(num)

    def __repr__(self):
        return self._num

    def __add__(self, other):
        return self._num + other._num

    def __lt__(self, other):
        return self + other < other + self


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        result = "".join(
            map(str, sorted([Number(n) for n in nums], reverse=True))
        )
        return "0" if result[0] == "0" else result


print(Solution().largestNumber([3, 30, 34, 5, 9]))
