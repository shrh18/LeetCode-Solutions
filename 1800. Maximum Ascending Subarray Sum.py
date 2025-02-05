class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxSum = nums[0]
        currSum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                currSum += nums[i]
                maxSum = max(maxSum, currSum)
            else:
                currSum = nums[i]

        return maxSum