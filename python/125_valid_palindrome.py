class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed = list(filter(lambda x: x.isalnum(), s))
        mid = len(processed) // 2

        for i in range(mid):
            if processed[i].lower() != processed[-i - 1].lower():
                return False
        return True
