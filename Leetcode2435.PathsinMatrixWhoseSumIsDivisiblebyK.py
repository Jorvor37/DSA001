class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # dp[j][r] = ways to reach current row, column j, with remainder r
        dp = [[0] * k for _ in range(n)]

        # Initialize (0, 0)
        first_r = grid[0][0] % k
        dp[0][first_r] = 1

        for i in range(m):
            new_dp = [[0] * k for _ in range(n)]
            for j in range(n):
                val = grid[i][j] % k
                for r in range(k):
                    new_r = (r + val) % k

                    # from top (dp[j])
                    if i > 0:
                        new_dp[j][new_r] = (new_dp[j][new_r] + dp[j][r]) % MOD

                    # from left (new_dp[j-1])
                    if j > 0:
                        new_dp[j][new_r] = (new_dp[j][new_r] + new_dp[j-1][r]) % MOD

                # handle the starting cell again: only for (0,0)
                if i == 0 and j == 0:
                    new_dp[0][first_r] = 1

            dp = new_dp  # move to next row

        return dp[n-1][0] % MOD
