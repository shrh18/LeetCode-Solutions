class ProductOfNumbers:

    def __init__(self):
        self.dp = []
        
    def add(self, num: int) -> None:
        if len(self.dp)==0:
            self.dp.append(num)
        else:
            if self.dp[-1] != 0:
                self.dp.append(num*self.dp[-1])
            else:
                self.dp.append(num)

        if num == 0:
            self.dp = [0]*len(self.dp)
            # self.dp[-1] = 1
       

    def getProduct(self, k: int) -> int:
        if k == len(self.dp):
            return 0 if self.dp[-1] * self.dp[0] == 0 else self.dp[-1]
        if self.dp[-1-k] == 0:
            if self.dp[-k] != 0:
                return self.dp[-1]
            else:
                return 0
        else:
            return self.dp[-1] // self.dp[-1-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)