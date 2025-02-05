class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        t1, t2 = None, None
        for i in range(len(s1)):
            if s1[i] != s2[i] and t1 is None:
                t1 = i
            elif s1[i] != s2[i] and t1 is not None:
                t2 = i
                break

        if t1 is None and t2 is None:
            return True
        if t1 is not None and t2 is None:
            return False

        s = ''.join([ s1[:t1], s1[t2], s1[t1+1:t2], s1[t1], s1[t2+1:] ])

        if s == s2:
            return True
        else:
            return False