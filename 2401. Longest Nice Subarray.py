class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 1
        
        l, r, n = 0, 1, len(nums)
        count = 1
        x = nums[l]

        while r < n:
            if x & nums[r] == 0:
                count = max(count, r-l+1)
                x |= nums[r]
                r += 1
            else:
                x ^= nums[l]
                l += 1

        return count