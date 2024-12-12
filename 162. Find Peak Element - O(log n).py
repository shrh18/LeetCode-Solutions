class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return 
        if len(nums)==1:
            return 0
        if len(nums)==2:
            if nums[0]>nums[1]:
                return 0
            else:
                return 1

        # runs in O(log n)
        self.maxVal = -math.inf
        self.maxInd = -1
        self.mid = -1

        def rec(l, r):
            if l>=r:
                if nums[l]>self.maxVal:
                    self.maxVal = nums[l]
                    self.maxInd = l
                return self.maxInd

            mid = (l+r)//2
            if nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]:
                self.mid = mid
                return mid

            rec(l, mid)
            rec(mid+1, r)

        rec(0, len(nums)-1)
        print(f"Mid is {self.mid} and maxInd is {self.maxInd}")
        if self.mid == -1:
            return self.maxInd
        return self.mid

            