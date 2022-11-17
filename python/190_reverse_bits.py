class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for _ in range(32):
            result <<= 1
            result += n % 2
            n >>= 1

        return result
