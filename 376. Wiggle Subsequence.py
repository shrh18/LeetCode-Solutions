class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            if nums[0] == nums[1]:
                return 1
            else:
                return 2

        i = 2
        while i<len(nums):
            if nums[i-2]>nums[i-1]<nums[i] or nums[i-2]<nums[i-1]>nums[i]:
                i += 1
                continue

            if nums[i-2] >= nums[i-1] >= nums[i] or nums[i-2] <= nums[i-1] <= nums[i]:
                del nums[i-1]
            else:
                i += 1

        if len(nums) == 2:
            if nums[0] == nums[1]:
                return 1
            else:
                return 2
    
        print(nums)
        return len(nums)