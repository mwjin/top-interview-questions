class Solution:
    def isHappy(self, n: int) -> bool:
        num_set = set()

        while n != 1:
            num_set.add(n)
            square_digit_sum = 0

            while n > 0:
                square_digit_sum += (n % 10) ** 2
                n //= 10

            if square_digit_sum in num_set:
                return False

            n = square_digit_sum

        return True


Solution().isHappy(2)
