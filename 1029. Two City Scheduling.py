class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ll = []
        cost = 0
        for i in range(len(costs)):
            ll.append([costs[i][0]-costs[i][1], i])

        ll = sorted(ll, key=lambda x:x[0])
        print(ll)

        for i in range(len(ll)//2):
            idx1, idx2 = ll[i][1], ll[-1-i][1]
            cost = cost + costs[idx1][0] + costs[idx2][1]

        return cost

        
            