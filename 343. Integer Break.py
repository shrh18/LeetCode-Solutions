class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        dp = [0]*(n+1)
        dp[1], dp[2], dp[3] = 1, 1, 2


        for i in range(2, n+1):
            for j in range(1, i-1):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])

        # print(dp)
        return dp[n]


