class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        gg = max(nums)
        for i in range(gg):
            if i not in nums:
                return i
        return gg+1