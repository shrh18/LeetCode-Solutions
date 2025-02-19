class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        s = ['a', 'b', 'c']
        ret = []

        def backtrack(st):
            if len(st)>=n:
                ret.append(st)
                return
            
            for ch in s:
                if st[-1] != ch:
                    st += ch
                    backtrack(st)
                    st = st[:-1]

        for ch in s:
            st = ch
            backtrack(st)

        print(ret)
        ret = sorted(ret)

        if k>len(ret):
            return ""
        else:
            return ret[k-1]
