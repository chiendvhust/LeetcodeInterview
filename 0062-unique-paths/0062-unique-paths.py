class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    dp[r][c] = 1
                elif r == 0:
                    dp[r][c] = dp[r][c - 1]
                elif c == 0:
                    dp[r][c] = dp[r - 1][c]
                else:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[m - 1][n - 1]