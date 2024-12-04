class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        def backtrack(st, formed):
            if len(formed) == k:
                ret.append(formed.copy())
            
            for i in range(st, n+1):
                formed.append(i)
                backtrack(i+1, formed)
                formed.pop()

        backtrack(1, [])
        return ret

