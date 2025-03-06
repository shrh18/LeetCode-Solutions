class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        R, C = len(matrix), len(matrix[0])
        if R == C == 1:
            if matrix[0][0] == "1":
                return 1
            else:
                return 0

        dp = [[0 for _ in range(C)]  for _ in range(R)]
        count = 0
        mm = 0
        for i in range(C):
            dp[0][i] = int(matrix[0][i])
            if matrix[0][i] == "1":
                count = 1
                mm = max(mm, int(matrix[0][i]))
        for i in range(R):
            dp[i][0] = int(matrix[i][0])
            if matrix[i][0] == "1":
                count = 1
                mm = max(mm, int(matrix[i][0]))

        for i in range(1, R):
            for j in range(1, C):
                if matrix[i][j] == "1":
                    count = 1
                    mm = max(mm, int(matrix[i][j]))
                if matrix[i][j] == matrix[i-1][j-1] == matrix[i-1][j] == matrix[i][j-1] == "1":
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    mm = max(mm, dp[i][j])
                else:
                    dp[i][j] = int(matrix[i][j])

        return mm**2


     
