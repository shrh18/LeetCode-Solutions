class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret = []
        intervals.sort()
        for arr in intervals:
            if len(ret)==0:
                ret.append(arr)
            else:
                if ret[-1][1]>=arr[0] and ret[-1][1]<=arr[1]:
                    xx = [ret[-1][0], arr[1]]
                    ret.pop()
                    ret.append(xx)
                elif ret[-1][1]>=arr[0] and ret[-1][1]>arr[1]:
                    xx = [ret[-1][0], ret[-1][1]]
                    ret.pop()
                    ret.append(xx)
                else:
                    ret.append(arr)
        return ret
        