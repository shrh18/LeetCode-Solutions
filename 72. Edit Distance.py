class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        for i in range(1, m+1):
            dp[0][i] = i

        for i in range(1, n+1):
            dp[i][0] = i

        for i in range(1, n+1):
            for j in range(1, m+1):
                x1 = dp[i-1][j] + 1
                x2 = dp[i][j-1] + 1
                x3 = dp[i-1][j-1] + 1 if word1[i-1] != word2[j-1] else dp[i-1][j-1]
                dp[i][j] = min(x1, x2, x3)

        return dp[-1][-1] 
        