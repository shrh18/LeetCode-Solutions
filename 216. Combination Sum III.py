class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ret = []

        def backtrack(st, n, k, formed):
            ff = formed.copy()
            if len(ff)== k and n==0:
                ret.append(ff)
                return
            if n<0:
                return

            for i in range(st, 10):

                ff.append(i)
                backtrack(i+1, n-i, k, ff)
                ff.pop()

        backtrack(1, n, k, [])
        return ret