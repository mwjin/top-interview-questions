from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for n in range(1, numRows + 1):
            if n == 1:
                result.append([1])
            elif n == 2:
                result.append([1, 1])
            else:
                prev = result[-1]
                curr = [1]
                for i in range(1, len(prev)):
                    curr.append(prev[i - 1] + prev[i])
                curr.append(1)
                result.append(curr)

        return result
