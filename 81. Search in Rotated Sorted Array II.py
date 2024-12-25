class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        self.ret = False
        def rec(l, r):
            if l>r:
                return
            
            mid = (l+r)//2
            if nums[mid]==target:
                self.ret = True
                return        

            if nums[l] == nums[mid] == nums[r]:
                l+=1
                r-=1
                return rec(l,r)
            
            if nums[l]<=nums[mid]:
                if nums[l] <= target < nums[mid]:
                    rec(l, mid-1)
                else:
                    rec(mid+1, r)
            else:
                if nums[mid]< target <= nums[r]:
                    rec(mid+1, r)
                else:
                    rec(l, mid-1)

        rec(0, len(nums)-1)
        return self.ret