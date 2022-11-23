from math import sqrt


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        is_prime = [True for _ in range(n)]
        is_prime[0] = is_prime[1] = False

        for num in range(2, int(sqrt(n)) + 1):
            if is_prime[num]:
                for mul in range(num * num, n, num):
                    is_prime[mul] = False

        return sum(is_prime)
