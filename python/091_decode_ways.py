class Solution:
    def numDecodings(self, s: str) -> int:
        self.s = s
        self.dp = [-1 for _ in range(len(s))]
        return self.numDecodingsInternal(0)

    def numDecodingsInternal(self, idx: int) -> int:
        if idx == len(self.s):
            return 1
        if self.s[idx] == "0":
            return 0
        if idx == len(self.s) - 1:
            return 1
        if self.dp[idx] != -1:
            return self.dp[idx]

        result = self.numDecodingsInternal(idx + 1)

        if int(self.s[idx : idx + 2]) <= 26:
            result += self.numDecodingsInternal(idx + 2)

        self.dp[idx] = result

        return result
