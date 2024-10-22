class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = set(nums)
        ret = []
        for i in range(1,n+1):
            if i not in nums:
                ret.append(i)
        return ret