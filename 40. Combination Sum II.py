class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort()
        
        def backtrack(arr, i, total):
            if total == target:
                ret.append(arr.copy())
                return
            if total>target or i>=len(candidates):
                return
            
            for k in range(i, len(candidates)):
                if k>i and candidates[k] == candidates[k-1]:
                    continue
                arr.append(candidates[k])
                backtrack(arr, k+1, total+candidates[k])
                arr.pop()

        backtrack([], 0, 0)
        return ret

