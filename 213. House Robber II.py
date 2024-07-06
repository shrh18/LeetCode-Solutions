class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0], nums[1])

        # choose first drop last
        maxAcc1 = [0]*(len(nums)-1)
        maxAcc1[0] = nums[0]
        maxAcc1[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)-1):
            maxAcc1[i] = max(maxAcc1[i-1], maxAcc1[i-2]+nums[i])
        max1 = maxAcc1[-1]

        # drop first choose last
        maxAcc2 = [0]*(len(nums)-1)
        maxAcc2[0] = nums[1]
        maxAcc2[1] = max(nums[1], nums[2])
        for i in range (3, len(nums)):
            maxAcc2[i-1] = max(maxAcc2[i-1-1], maxAcc2[i-2-1]+nums[i])
        max2 = maxAcc2[-1]

        return (max(max1, max2))

        