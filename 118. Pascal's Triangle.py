class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = []
        self.prev = []

        def rec(n, prevarr):
            arr = [1]*(len(prevarr)+1)
            for i in range(1, len(prevarr)):
                arr[i] = prevarr[i] + prevarr[i-1]
            ret.append(arr)
            self.prev = arr

        for i in range(1, numRows+1):
            rec(numRows, self.prev)

        return ret
