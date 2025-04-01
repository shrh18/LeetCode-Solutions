class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
       
        diff = []
        for i in range(1, len(weights)):
            diff.append(weights[i] + weights[i-1])
            
        diff.sort()

        mn, mx = 0, 0
        for i in range(k-1):
            mn += diff[i]
            mx += diff[-i-1]

        return mx-mn
