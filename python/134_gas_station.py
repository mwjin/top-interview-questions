from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        remain = [gas[i] - cost[i] for i in range(len(gas))]
        for i in range(1, len(remain)):
            remain[i] += remain[i - 1]

        if remain[-1] < 0:
            return -1

        min_idx = 0
        for i in range(len(remain)):
            if remain[i] < remain[min_idx]:
                min_idx = i
        return (min_idx + 1) % len(remain)


Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
