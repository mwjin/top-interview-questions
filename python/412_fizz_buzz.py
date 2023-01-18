from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = [None for _ in range(n)]
        strs = ["", "Fizz", "Buzz", "FizzBuzz"]

        for i in range(1, n + 1):
            mod = 0
            if i % 3 == 0:
                mod += 1
            if i % 5 == 0:
                mod += 2

            result[i - 1] = strs[mod] if mod else str(i)

        return result
