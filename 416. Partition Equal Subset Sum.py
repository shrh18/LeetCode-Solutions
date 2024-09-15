class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1:
            return False
        
        target = sum(nums)/2
        dp = set()
        dp.add(0)
        
        for i in range(len(nums)-1, -1, -1):
            newdp = dp.copy()
            for num in dp:
                newdp.add(num+nums[i])
            dp = newdp

        if target in dp:
            return True
        else:
            return False 