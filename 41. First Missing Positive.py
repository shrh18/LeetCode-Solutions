class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxnum = max(nums)
        print(maxnum)
        for i in range(1, maxnum):
            if i not in numset:
                return i
        
        if maxnum<0:
            return 1
        return maxnum+1