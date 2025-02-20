class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        direc = [(0,1),(1,0)]
        R, C = len(grid), len(grid[0])
        dp = [[0 for i in range(C)] for j in range(R)]
        self.mm = math.inf

        dp[0][0] = grid[0][0]
        for i in range(1, C):
            dp[0][i] = grid[0][i] + dp[0][i-1]
        for i in range(1, R):
            dp[i][0] = grid[i][0] + dp[i-1][0]

        for i in range(1, R):
            for j in range(1, C):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        print(dp)
        return dp[-1][-1]
