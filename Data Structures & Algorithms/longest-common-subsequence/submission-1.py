class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m, n = len(text1), len(text2)

        # Create DP matrix with an extra row and column.
        # dp[i][j] represents the LCS length of
        # text1[i:] and text2[j:].
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Traverse both strings from right to left.
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                # If characters match, include this character
                # and move both indices forward.
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]

                # If characters don't match, explore both options:
                # Skip a character from text1 or skip from text2.
                else:
                    dp[i][j] = max(
                        dp[i + 1][j],
                        dp[i][j + 1]
                    )

        # The answer is stored at the top-left cell.
        return dp[0][0]