class Solution:

    def __init__(self, w: List[int]):
        self.idxs = [None]
        self.idxs[0] = [1, w[0]]
        for i in range(1, len(w)):
            self.idxs.append([self.idxs[i-1][1]+1, self.idxs[i-1][1]+w[i]])

    def pickIndex(self) -> int:
        idx = random.randint(1, self.idxs[-1][1])
        
        for i in range(len(self.idxs)):
            if self.idxs[i][0]<=idx<=self.idxs[i][1]:
                return i

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()