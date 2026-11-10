class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                continue
            dp[i] = dp[i + 1] # we have only the number of ways of that 1
            if i + 1 < n and 10 <= int(s[i : i + 2]) <= 26:
                dp[i] += dp[i + 2] #for this we have already the number of ways for single digit so we do dp[i]+
        return dp[0]
        