class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            match = 0
            while match < len(needle) and haystack[i + match] == needle[match]:
                match += 1
            if match == len(needle):
                return i
        return -1
