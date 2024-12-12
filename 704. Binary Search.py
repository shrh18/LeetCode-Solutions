class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def rec(l,r):
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if l>=r:
                return -1
            if target<nums[mid]:
                return rec(l, mid)
            else:
                return rec(mid+1, r)

        return rec(0, len(nums)-1)