class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        import bisect
        fz = bisect.bisect_left(nums, 0)
        fo = bisect.bisect_left(nums, 1)

        return max(fz, len(nums)-fo)