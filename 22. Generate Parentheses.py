class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        ss = 0
        paren = []
        for _ in range(n):
            paren.append("(")
            paren.append(")")
        print(paren)

        def backtrack(openCount, closedCount, arr, start, bal):
            if bal<0:
                return
            kk = copy.copy(arr)
            if openCount == n and closedCount == n:
                ret.append(kk)
            
            for j in range(start, len(paren)):
                if openCount<n:
                    kk+="("
                    backtrack(openCount+1, closedCount, kk, j+1, bal+1)
                    kk = kk[:-1]
                if closedCount<n:
                    kk+=")"
                    backtrack(openCount, closedCount+1, kk, j+1, bal-1)
                    kk = kk[:-1]

        backtrack(0, 0, "", 0, 0)
        return ret


