class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        dp [0][0] = triangle[0][0]
        for i in range(1, n):
            dp[i][0] = triangle[i][0] + dp[i-1][0]
            dp[0][i] = triangle[i][-1] + dp[0][i-1]

        for i in range(1, n):
            for j in range(1, n):
                if i+j<n:
                    dp[i][j] = triangle[i+j][j] + min(dp[i-1][j], dp[i][j-1])
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1])

        print(dp)
        return dp[-1][-1]