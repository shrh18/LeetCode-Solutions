class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        mul2p = defaultdict(int)         
       
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                mul2p[nums[i]*nums[j]] += 1

        ret = 0
        for k, v in mul2p.items():
            if v>1:
                ret += (math.factorial(v)) // (math.factorial(v-2)) * 4

        return ret


