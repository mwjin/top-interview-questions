class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed = list(filter(lambda x: x.isalnum(), s.lower()))
        return processed == processed[::-1]
