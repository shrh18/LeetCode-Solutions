class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        
        index = {x:i for i,x in enumerate(arr)}
        n = len(arr)
        maxlen = 0
        dp = [[2]*n for _ in range(n)]

        for i in range(n):
            for j in range(i):
                req = arr[i] - arr[j]
                if req in index and index[req] < j:
                    k = index[req]
                    dp[j][i] = dp[k][j] + 1
                    maxlen = max(maxlen, dp[j][i])

        return maxlen if maxlen>=3 else 0
