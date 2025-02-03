class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if len(nums) == 2:
            return False if nums[0]%2 == nums[1]%2 else True

        for j in range(1, len(nums)):
            if nums[j]%2 == nums[j-1]%2:
                return False 
            else:
                continue

        return True
        