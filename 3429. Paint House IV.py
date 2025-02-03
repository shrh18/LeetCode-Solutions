class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        mid = n//2
        if mid == 0:
            return 0
        
        dpPrev = {}
        for c in range(3):
            for d in range(3):
                if c!=d:
                    dpPrev[(c,d)] = cost[mid-1][c] + cost[mid][d]

        for k in range(1, mid):
            dpCurr = {}
            i, j = mid-1-k, mid+k
            for (prevC, prevD) in dpPrev:
                for currC in range(3):
                    if currC == prevC:
                        continue
                    for currD in range(3):
                        if currD == prevD or currD == currC:
                            continue
                        totalCost = dpPrev[(prevC,prevD)] + cost[i][currC] + cost[j][currD]
                        key = (currC, currD)
                        if key not in dpCurr or totalCost < dpCurr[key]:
                            dpCurr[key] = totalCost
            dpPrev = dpCurr
        return min(dpPrev.values())
        