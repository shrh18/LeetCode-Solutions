class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ret = []
        b2c = defaultdict(int)
        c2b = defaultdict(set)

        for b, c in queries:
            prevbc = b2c[b]
            b2c[b] = c
            
            if prevbc in c2b:
                c2b[prevbc].remove(b)
                if len(c2b[prevbc]) == 0:
                    del c2b[prevbc]
            c2b[c].add(b)
            # print(b2c)
            # print(c2b)
            ret.append(len(c2b))

        return ret