class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        np = 0
        nn = {}
        for i in nums:
            if i in nn:
                nn[i]+=1
            else:
                nn[i]=1
        
        for k,v in nn.items():
            if v==1:
                return k