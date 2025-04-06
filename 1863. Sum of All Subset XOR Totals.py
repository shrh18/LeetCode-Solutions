class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        tot = 0
        n = len(nums)
        self.tot = 0

        def rec(i, ss):
            if i >= n:
                return
            
            ss ^= nums[i]
            print(ss)
            self.tot += ss
            rec(i+1, ss)
            ss ^= nums[i]
            rec(i+1, ss)

        rec(0, 0)

        return self.tot