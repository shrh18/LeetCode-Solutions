class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        self.maxi = 0
        def rec(l, r):
            mid = (l+r)//2
            if arr[mid]>self.maxi:
                self.maxi = arr[mid]
            if l>r:
                return
            if arr[mid]<arr[mid+1]:
                rec(mid+1, r)
            else:
                rec(l, mid-1)
        
        rec(0, len(arr)-1)
        return arr.index(self.maxi)
