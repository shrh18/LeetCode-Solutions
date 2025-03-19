class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0

        for i in range(len(nums)-2):
            if nums[i] == 0:
                nums[i] ^= 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
                ops += 1

        if nums[-1] == nums[-2] == nums[-3]:
            return ops
        else:
            return -1

