class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:

        def rec(ret, ss, l):
            if l == len(ret):
                return ret, True
            if ret[l] is not None:
                return rec(ret, ss, l+1)
            
            for i in sorted(ss, reverse=True):
                if i ==1 :
                    ret[l] = i
                    ss.remove(i)
                    res, suc = rec(ret, ss, l+1)
                    if suc:
                        return res, True
                    ret[l] = None
                    ss.add(i)
                else:
                    if l+i<len(ret) and ret[l+i] is None:
                        ret[l] = i
                        ret[l+i] = i
                        ss.remove(i)
                        res, suc = rec(ret, ss, l+1)
                        if suc:
                            return res, True
                        ret[l] = None
                        ret[l+i] = None
                        ss.add(i)
                   
            return None, False

        ret = [None]*(2*(n-1)+1)
        ss = set(range(1, n+1))
        res, suc = rec(ret, ss, 0)
        if suc:
            return res

        return -1
