class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==0:
            return ""
        if len(s)==1:
            return s
        slen = len(s)
        dp = [[ 0 for _ in range(slen)] for _ in range(slen)]
        maxLength = 1
        start = 0
        for i in range(slen):
            dp[i][i] = True
        for i in range(slen-1):
            if s[i]==s[i+1]:
                dp[i][i+1] = True
                start = i
                maxLength = 2
        
        for length in range(3, slen+1):
            for i in range(slen-length+1):
                j = i+length-1
                if s[i]==s[j] and dp[i+1][j-1]==True:
                    dp[i][j] = True
                    start = i
                    maxLength = length

        return s[start: start+maxLength]