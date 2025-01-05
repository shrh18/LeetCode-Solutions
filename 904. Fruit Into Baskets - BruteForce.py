class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) < 3: return len(fruits)
        # Gives TLE
        mm = 0
        ss = set()
        l, r = 0, 1
        ss.add(fruits[0])
        ss.add(fruits[1])
        ll = 2
        while r<len(fruits)-1:
            if fruits[r+1] in ss and len(ss)<2:
                r += 1
                ll = r-l+1
                ss = set(fruits[l:r+1])
            elif fruits[r+1] not in ss and len(ss)<2:
                r += 1
                ss = set(fruits[l:r+1])
                ll = r-l+1
            elif fruits[r+1] not in ss and len(ss)==2:
                ss.remove(fruits[l])
                l += 1
                ss = set(fruits[l:r+1])
                ll = r-l+1
            elif fruits[r+1] in ss and len(ss)==2:
                r += 1
                ll = r-l+1
                ss = set(fruits[l:r+1])
            if ll>mm:
                mm = ll
                return mm
