class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            if piles[0]>=h:
                return math.ceil(piles[0]/h)
            else:
                return 1
        mm = max(piles)
        ret = math.inf
        n = len(piles)
        if n == h:
            return mm
        
        def bs(start, end, ss):
            if start == end and ss<=h:
                return start
            ss = 0
            mid = (start+end)//2
            for num in piles:
                ss += math.ceil(num/mid)
                if ss>h:
                    break

            if ss>h:
                return bs(mid+1, end, ss)
            else:
                return bs(start, mid, ss)

        return bs(1, mm+1, 0)
            

