class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        ret = []
        n = len(nums)
        nums.sort()
        def backtrack(arr, rem):
            if len(arr)==n:
                ret.append(arr[:])
                return
            for i in range(len(rem)):
                temp = i
                while i+1<len(rem) and rem[i]==rem[i+1]:
                    i+=1
                rr = rem[:temp]+rem[i+1:]
                backtrack(arr+[rem[temp]], rr)

        backtrack([], nums)
        return ret
        