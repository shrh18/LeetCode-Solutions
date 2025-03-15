class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        ss = sum(candies)
        if k>ss:
            return 0
        if k == ss:
            return 1

        def bs(l, r):
            if l>r:
                return r

            mid = (l+r)//2
            count = 0
            for num in candies:
                count += num//mid

            if count >= k:
                return bs(mid+1, r)
            elif count < k:
                return bs(l, mid-1)
            
        return bs(1, max(candies))