class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return ""
        
        ef = {}
        for c in s:
            if c in ef:
                ef[c]+=1
            else:
                ef[c]=1

        nef = dict(sorted(ef.items(), key=lambda x:x[1], reverse=True))
        print(nef)
        ret=""
        for l,c in nef.items():
            for k in range(c):
                ret=ret+l
        return ret

