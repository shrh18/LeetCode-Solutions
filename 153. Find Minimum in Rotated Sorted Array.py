class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<nums[-1]:
            return nums[0]
        def rec(l,r):
            if l>=r:
                return nums[l]
            mid = (l+r)//2
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            if nums[mid]<nums[mid-1]:
                return nums[mid]
            
            if nums[mid]>nums[r]:
                return rec(mid+1, r)
            else:
                return rec(l, mid)

        return rec(0, len(nums)-1)
