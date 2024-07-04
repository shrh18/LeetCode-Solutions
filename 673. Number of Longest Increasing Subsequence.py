class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp={}
        lisLen, ret = 0,0
        for i in range(len(nums)-1, -1, -1):
            maxLen, maxCount = 1, 1
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j]:
                    length, count = dp[j]
                    if length+1>maxLen:
                        maxLen, maxCount = length+1, count
                    elif length+1==maxLen:
                        maxCount+=count
            
            if maxLen>lisLen:
                lisLen, ret = maxLen, maxCount
            elif maxLen==lisLen:
                ret+=maxCount
            dp[i] = [maxLen, maxCount]
        print(dp)
        return ret
        
        