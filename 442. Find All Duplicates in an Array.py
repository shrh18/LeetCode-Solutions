class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nn = set()
        ret = []
        for i in nums:
            if i in nn:
                ret.append(i)
            else:
                nn.add(i)
        return ret