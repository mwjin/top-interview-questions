from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for n in nums:
            if n not in counter:
                counter[n] = 0
            counter[n] += 1

        result = sorted(counter.items(), key=lambda item: item[1], reverse=True)
        return [e for e, _ in result[:k]]
