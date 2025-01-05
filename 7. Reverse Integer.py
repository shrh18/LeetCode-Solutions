class Solution:
    def reverse(self, x: int) -> int:
        ss = str(x)
        neg = False
        int32 = pow(2, 32)//2 
        if ss[0] == '-': 
            neg = True
            ss = ss[1:]

        ret = 0
        k = 0
        for ch in ss:
            ret += int(ch)*(pow(10, k))
            k += 1
        
        if neg:
            ret = 0 - ret

        if -int32 <= ret <= int32 -1:
            return ret
        else:
            return 0

        
        