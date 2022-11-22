class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_square_digits(n):
            result = 0

            while n > 0:
                result += (n % 10) ** 2
                n //= 10

            return result

        slow = n
        fast = sum_square_digits(sum_square_digits(n))

        while slow != fast:
            slow = sum_square_digits(slow)
            fast = sum_square_digits(sum_square_digits(fast))

        return slow == 1
