class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        start = 0
        result = 0

        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                result = max(result, i - start + 1)
            used[c] = i

        return result


print(Solution().lengthOfLongestSubstring("tmmzuxt"))
