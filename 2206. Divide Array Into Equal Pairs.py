class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums = sorted(nums)

        while len(nums)>1:
            if nums[-1] == nums[-2]:
                nums.pop()
                nums.pop()
            else:
                return False

        return True if len(nums) == 0 else False
            