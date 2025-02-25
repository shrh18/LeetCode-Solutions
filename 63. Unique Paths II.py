class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R, C = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        dp = [[0 for _ in range(C)] for _ in range(R)]
        dp[0][0] = 1

        r, c = False, False
        for i in range(1, C):
            if obstacleGrid[0][i] == 1:
                c = True 
            dp[0][i] = 1 if not c else 0

        for i in range(1, R):
            if obstacleGrid[i][0] == 1:
                r = True
            dp[i][0] = 1 if not r else 0

        for r in range(1, R):
            for c in range(1, C):
                dp[r][c] = dp[r-1][c] + dp[r][c-1] if obstacleGrid[r][c] == 0 else 0

        return dp[-1][-1]
