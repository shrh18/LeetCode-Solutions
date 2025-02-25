class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        pre = [0]*(len(arr)+1)
        odds, evens = 0, 0
        for i in range(len(arr)):
            pre[i+1] = pre[i] + arr[i]
            if pre[i+1] % 2 == 1:
                odds += 1
            else:
                evens += 1

        return ((evens*odds)+odds) % MOD

        