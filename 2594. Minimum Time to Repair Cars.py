class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 1, ((cars)**2)*(max(ranks))

        def bs(l, r):

            if l>r:
                return l
            
            mid = (l+r)//2
            ss = 0
            for rank in ranks:
                ss += math.floor(math.sqrt(mid//rank))

            
            if ss < cars:
                return bs(mid+1, r)
            elif ss >= cars:
                return bs(l, mid-1)

        return bs(l, r)
