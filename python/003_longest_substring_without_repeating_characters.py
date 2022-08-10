class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        maxStart = start = 0
        maxEnd = end = 0
        charSet = set()

        while end < len(s):
            while s[end] in charSet:
                charSet.remove(s[start])
                start += 1

            charSet.add(s[end])
            if maxEnd - maxStart < end - start:
                maxStart = start
                maxEnd = end
            end += 1

        return maxEnd - maxStart + 1
