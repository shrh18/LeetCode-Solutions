class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        
        dep = {i:set() for i in range(n)}
        for f,s in edges:
            dep[f].add(s)
            dep[s].add(f)

        def countleaves():
            leaves = []
            for k,v in dep.items():
                if len(v)==1:
                    leaves.append(k)
            return leaves
        
        def removeleaves(leaves):
            for k in leaves:
                nei = next(iter(dep[k]))
                dep[nei].remove(k)
                del dep[k]

        while len(dep)>2:
            removeleaves(countleaves())

        return list(dep.keys())