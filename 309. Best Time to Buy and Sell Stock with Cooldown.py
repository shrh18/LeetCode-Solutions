class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        if l<=1:
            return 0
        if l==2:
            if prices[1]>prices[0]:
                return prices[1]-prices[0]
            else: return 0

        
        # use cache with dict
        dp = {} # (i, buying) -> profitVal
    
        # We use recursion

        def dfs(i, buying):
            if i>=l:
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i+1, buying)
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
        
            return dp[(i, buying)]

        return dfs(0, True)