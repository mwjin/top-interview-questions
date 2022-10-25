from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        min_cumulative_gas = cumulative_gas = gas[0] - cost[0]
        min_idx = 0

        for i in range(1, len(gas)):
            cumulative_gas += gas[i] - cost[i]
            if min_cumulative_gas > cumulative_gas:
                min_cumulative_gas = cumulative_gas
                min_idx = i

        return (min_idx + 1) % len(gas) if cumulative_gas >= 0 else -1


print(Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
