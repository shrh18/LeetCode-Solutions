class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []

        def backtrack(arr, i, total):
            if total == target:
                ret.append(arr.copy())
                return
            if total>target or i>=len(candidates):
                return
            
            arr.append(candidates[i])
            total+=candidates[i]
            backtrack(arr, i, total)
            t = arr.pop()
            total-=t
            backtrack(arr, i+1, total)

        backtrack([], 0, 0)
        return ret

