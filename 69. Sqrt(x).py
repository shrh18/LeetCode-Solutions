class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        if x==1:
            return 1
        l, r = 0, x
        mid = (l+r)/2
        while r>mid and l<mid:
            tempsq = int(mid)*int(mid)
            if tempsq == x:
                return int(mid)
            if tempsq<x:
                l=mid
                mid = int((l+r)/2)
            if tempsq>x:
                r=mid
                mid = int((l+r)/2)    
        return mid
            
        