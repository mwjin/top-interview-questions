class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1

        start, end = 0, x

        while end - start > 1:
            mid = start + (end - start) // 2
            sqr = mid ** 2
            if sqr == x:
                return mid
            elif sqr < x:
                start = mid
            else:
                end = mid

        return start


print(Solution().mySqrt(9))
print(Solution().mySqrt(7))
print(Solution().mySqrt(5))
print(Solution().mySqrt(4))
print(Solution().mySqrt(2))
print(Solution().mySqrt(1))
