class Solution:
    def countAndSay(self, n: int) -> str:
        
        def rle(n):
            if n == 1:
                return ['1']
            
            s = rle(n-1)
            l, r, count, ll = 0, 0, 0, len(s)
            ss = []
            while r<ll:
                while r<ll and s[r] == s[l]:
                    count += 1
                    r += 1
    
                ss.append(str(count))
                count = 0
                ss.append(s[l])
                l = r
            
            return ss

        return "".join(rle(n))