class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ret = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        for num in nums:
            if num != 0:
                ret.append(num)

        while len(ret) != len(nums):
            ret.append(0)

        return ret