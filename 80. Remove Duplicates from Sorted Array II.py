class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # count = 1
        # i = 1
        # while i<len(nums):
        #     if nums[i] == nums[i-1]:
        #         count += 1
        #         if count>2:
        #             while i<len(nums) and nums[i] == nums[i-1]:
        #                 del nums[i]
        #             count = 1
        #     else:
        #         count = 1
        #     i += 1

        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k+=1

        return k