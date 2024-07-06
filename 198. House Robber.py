class Solution:
    def rob(self, nums: List[int]) -> int:
        maxAcc = [0]*(len(nums))
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0], nums[1])

        maxAcc[0]=nums[0]
        maxAcc[1]= max(nums[0], nums[1])

        for i in range(2, len(nums)):
            maxAcc[i] = max(maxAcc[i-1], maxAcc[i-2]+nums[i])
            print(maxAcc[i])
        print(maxAcc[-1])
        return maxAcc[-1]