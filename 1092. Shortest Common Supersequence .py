class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        R, C = len(str1), len(str2)
        dp = [[0]*(C+1) for _ in range(R+1)]

        for i in range(1, R+1):
            for j in range(1, C+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        i, j = R, C
        scs = []
        while i>0 and j>0:
            if str1[i-1] == str2[j-1]:
                scs.append(str1[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                scs.append(str1[i-1])
                i -= 1
            else:
                scs.append(str2[j-1])
                j -= 1

        while i>0:
            scs.append(str1[i-1])
            i -= 1
        while j>0:
            scs.append(str2[j-1])
            j -= 1

        return "".join(scs[::-1])
