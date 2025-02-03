class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        l, r = 0, 1

        maxLinc = 1
        maxLdec = 1
        currLinc = 1
        currLdec = 1
        while r < len(nums):
            if nums[l] < nums[r]:
                currLinc += 1
                maxLinc = max(maxLinc, currLinc)
            else:
                currLinc = 1

            if nums[l] > nums[r]:
                currLdec += 1
                maxLdec = max(maxLdec, currLdec)
            else:
                currLdec = 1

            l += 1
            r += 1

        return max(maxLinc, maxLdec)