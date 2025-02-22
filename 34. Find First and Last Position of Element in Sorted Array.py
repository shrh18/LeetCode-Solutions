class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        ret = [-1, -1]

        def left(l, r):
            while l<=r:
                mid = (l+r)//2
                if nums[mid] == target:
                    if mid == 0 or nums[mid-1]<target:
                        ret[0] = mid
                        return
                    r = mid-1
                elif nums[mid]<target:
                    l = mid+1
                elif nums[mid]>target:
                    r = mid-1
            
        def right(l, r):
            while l<=r:
                mid = (l+r)//2
                if nums[mid] == target:
                    if mid == len(nums)-1 or nums[mid+1]>target:
                        ret[1] = mid
                        return
                    l = mid+1
                elif nums[mid]<target:
                    l = mid+1
                elif nums[mid]>target:
                    r = mid-1

        left(0, len(nums)-1)
        right(0, len(nums)-1)
        return ret

            
