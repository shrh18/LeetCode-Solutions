class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        ret = []
        n = len(nums)

        def backtrack(arr, rem):
            if len(arr)==n:
                ret.append(arr[:])
                return
            for i in range(len(rem)):
                rr = rem[:i]+rem[i+1:]
                backtrack(arr+[rem[i]], rr)

        backtrack([], nums)
        return ret
        