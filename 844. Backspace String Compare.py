class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ns, nt = "", ""
        for ch in s:
            if ch == "#":
                ns = ns[:-1]
            else:
                ns+=ch
        
        for ch in t:
            if ch == "#":
                nt = nt[:-1]
            else:
                nt+=ch

        if ns == nt:
            return True

        return False