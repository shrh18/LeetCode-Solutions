class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        ret = []
        ret.append([])
        n = len(nums)
        
        def inset(arr, idx):
            gg = copy.deepcopy(arr)
            if idx>n-1:
                return
            gg.append(nums[idx])
            if gg not in ret:
                ret.append(gg)
            inset(gg, idx+1)
            notinset(gg, idx+1)

        def notinset(arr, idx):
            if idx>n-1:
                return
            if arr not in ret:
                ret.append(arr)
            inset(arr, idx+1)
            notinset(arr, idx+1)
        
        inset([],0) 
        notinset([],0)
        return ret
        