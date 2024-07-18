class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        ret = []
        prev = lower-1
        for num in nums+[upper+1]:
            if num-prev>1:
                ret.append([prev+1, num-1])
            prev=num
        return ret 