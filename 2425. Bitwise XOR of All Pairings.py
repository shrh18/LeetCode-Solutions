class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        r1, r2 = 0, 0
        for num in nums1:
            r1 ^= num
        for num in nums2:
            r2 ^= num
        rr1, rr2 = 0 ,0
        for _ in range(len(nums2)):
            rr1 = rr1 ^ r1

        for _ in range(len(nums1)):
            rr2 = rr2 ^ r2

        return rr1^rr2