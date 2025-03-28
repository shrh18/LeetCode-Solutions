class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        l, r = 0, 2
        count = 0
        n = len(nums)
        flag = False
        while r < n:
            while r<n and nums[r] - nums[r-1] == nums[r-1] - nums[r-2]:
                r += 1
            if r>l:
                mm = r-l
                for i in range(3, r-l+1):
                    count += mm - i + 1
                flag = True
                l = r-1
                r = l+2

            if not flag:
                r += 1
                l += 1
            else:
                flag = False            

        return count
