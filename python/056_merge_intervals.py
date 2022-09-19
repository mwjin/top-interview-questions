from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda x: x[0])
        merged = list(intervals[0])

        for interval in intervals:
            if merged[0] <= interval[0] <= merged[1]:
                merged[1] = max(merged[1], interval[1])
            else:
                result.append(merged)
                merged = interval

        result.append(merged)

        return result
