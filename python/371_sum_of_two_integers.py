class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = lambda n: n & 0xFFF
        signed = lambda n: n & 0x800 == 0x800
        sum = mask(a ^ b)
        carry = mask((a & b) << 1)

        while carry:
            sum, carry = mask(sum ^ carry), mask((sum & carry) << 1)

        if signed(sum):
            sum ^= ~0xFFF

        return sum
