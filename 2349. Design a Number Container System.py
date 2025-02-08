class NumberContainers:

    def __init__(self):
        self.cont1 = defaultdict(int) # idx to num
        self.cont2 = defaultdict(list)
        self.valid = {}
        
    def change(self, index: int, number: int) -> None:
        if index in self.cont1:
            prev = self.cont1[index]
            if prev != number:
                self.valid[(prev, index)] = False

        self.cont1[index] = number
        heapq.heappush(self.cont2[number], index)
        self.valid[(number, index)] = True
        
    def find(self, number: int) -> int:
        if number not in self.cont2:
            return -1

        while self.cont2[number]:
            idx = self.cont2[number][0]    
            if self.valid.get((number, idx), False):
                return idx
            heapq.heappop(self.cont2[number])
        
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)