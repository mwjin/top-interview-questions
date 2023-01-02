class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        power = 1

        while power < n:
            power *= 3

        return power == n
