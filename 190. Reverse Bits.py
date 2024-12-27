class Solution:
    def reverseBits(self, n: int) -> int:
        arr = deque(list(str(bin(n))[2:]))
        self.ret = 0
        p = 0
        print(arr)
        for _ in range(32-len(arr)):
            arr.appendleft('0')
        for r in arr:
            self.ret += (int(r)*(pow(2, p)))
            p+=1
        
        return self.ret
        