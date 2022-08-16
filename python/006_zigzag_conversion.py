class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        result = [[] for _ in range(numRows)]
        row_idx = 0
        up = False

        for c in s:
            result[row_idx].append(c)
            if row_idx == 0 or row_idx == numRows - 1:
                up = ~up
            row_idx += 1 if up else -1

        return "".join(["".join(row) for row in result])


print(Solution().convert("AB", 1))
