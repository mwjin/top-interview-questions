from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = list(digits)
        carry = 1
        idx = len(result) - 1

        while carry and idx >= 0:
            sum = result[idx] + carry
            carry, result[idx] = sum // 10, sum % 10
            idx -= 1

        return [1, *result] if carry else result


print(Solution().plusOne([9, 9, 9]))
