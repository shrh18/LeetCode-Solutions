class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1]*n
        suf = [1]*n
        ret = [0]*n
        for i in range(1,n):
            pre[i] = pre[i-1]*nums[i-1]
            suf[n-1-i] = suf[n-i]*nums[n-i]
        print(pre)
        print(suf)
        for i in range(n):
            ret[i] = pre[i]*suf[i]
        print(ret)
        return ret
