class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ret = []
        self.prev = []

        def rec(n, prevarr):
            arr = [1]*(len(prevarr)+1)
            for i in range(1, len(prevarr)):
                arr[i] = prevarr[i] + prevarr[i-1]
            ret.append(arr)
            self.prev = arr

        for i in range(1, rowIndex+2):
            rec(rowIndex, self.prev)

        return ret[-1]

        