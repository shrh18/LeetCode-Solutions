class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return 
        if len(nums)==1:
            return 0
        if len(nums)==2:
            if nums[0]>nums[1]:
                return 0
            else:
                return 1

        maxVal = nums[0]
        maxInd = 0

        for i in range(1, len(nums)-1):
            val = nums[i]
            prev = nums[i-1]
            post = nums[i+1]
            if prev<val and val>post:
                return i
            if val>maxVal:
                maxVal = val
                maxInd = i

        if nums[-1]>maxVal:
            return len(nums)-1
        return maxInd
