import math
from collections import defaultdict
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        ret = []
        n = len(nums)
        nums.sort()
        def backtrack(arr, idx):
            gg = copy.deepcopy(arr)
            if idx==n:
                ret.append(gg)
                return
            gg.append(nums[idx])
            backtrack(gg, idx+1)
            gg.pop()
            while idx+1<n and nums[idx]==nums[idx+1]:
                idx+=1
            backtrack(gg, idx+1)
        
        backtrack([],0) 
        return ret
        