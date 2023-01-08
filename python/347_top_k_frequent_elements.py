from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [None for _ in range(len(nums) + 1)]
        counter = {}

        for n in nums:
            if n not in counter:
                counter[n] = 0
            counter[n] += 1

        for n, freq in counter.items():
            if bucket[freq] is None:
                bucket[freq] = []
            bucket[freq].append(n)

        result = []
        idx = len(nums)

        while k > 0:
            if bucket[idx] is not None:
                result.extend(bucket[idx])
                k -= len(bucket[idx])
            idx -= 1

        return result
