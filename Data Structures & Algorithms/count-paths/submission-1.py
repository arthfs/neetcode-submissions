class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        if m == 1 and n ==1:
            return 1

        for i in range(n):
            temp = [0] * m
            dp.append(temp.copy())

        for j in range(1, m):
            dp[0] [j] = 1

        for i in range(1, n):
            dp[i] [0] = 1

        for i in range(1, n-1):
            for j in range(1, m):
                dp[i] [j] = dp[i] [j-1] + dp[i-1] [j]

        for j in range(1, m):
            dp[n-1] [j] = dp[n-1] [j-1] + dp[n-2] [j]

        return dp[n-1] [m-1]