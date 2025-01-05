class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) < 3: return len(fruits)

        fruitCount = defaultdict(int)
        l = 0
        maxFruits = 0
        
        for r in range(len(fruits)):
            fruitCount[fruits[r]] += 1

            while len(fruitCount)>2:
                fruitCount[fruits[l]] -= 1
                if fruitCount[fruits[l]] == 0:
                    del fruitCount[fruits[l]]
                l += 1

            maxFruits = max(maxFruits, r-l+1)

        return maxFruits
            
                