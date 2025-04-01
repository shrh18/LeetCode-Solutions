class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0]*(n+1)

        dp[n-1] = questions[n-1][0]
        dp[n-2] = questions[n-2][0]

        for i in range(n-1, -1, -1):
            if i + questions[i][1] + 1 < n:
                dp[i] = max(questions[i][0] + dp[i + questions[i][1] + 1], dp[i+1])
            else:
                dp[i] = max(questions[i][0], dp[i+1])

        return dp[0]
