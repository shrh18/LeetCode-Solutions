class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        def binSearch(l, r):
            if l == r:
                return l

            mid = (l+r)//2
            cap = mid
            count = 1
            s = 0

            for weight in weights:
                if s + weight > cap:
                    count += 1
                    s = weight
                else:
                    s += weight

            if count <= days:
                return binSearch(l, mid)
            else:
                return binSearch(mid+1, r)

        return binSearch(l, r)