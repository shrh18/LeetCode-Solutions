class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:

        count = 0
        PreSum = [0]*(len(nums)+1)
        for i in range(len(nums)):
            PreSum[i+1] = PreSum[i]+nums[i]

        def merge(low, high):
            if high-low<=1:
                return 0

            mid = (high+low)//2
            count = merge(low, mid) + merge(mid, high)

            j=k=mid
            for left in PreSum[low:mid]:
                while j<high and PreSum[j]-left < lower:
                    j+=1
                while k<high and PreSum[k]-left <= upper:
                    k+=1
                count+= (k-j)
        
            PreSum[low:high] = sorted(PreSum[low:high])
            return count

        return merge(0, len(PreSum))