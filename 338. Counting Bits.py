class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            binary = list(bin(i))[2:]
            count = 0
            for ch in binary:
                if ch=='1':
                    count+=1
            ans.append(count)
        return ans