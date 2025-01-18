class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, maxR, steps = 0, 0, 0
        for i in range(len(nums)-1):
            maxR = max(maxR, i + nums[i])
            if i == steps:
                jumps += 1
                steps = maxR
        return jumps
        