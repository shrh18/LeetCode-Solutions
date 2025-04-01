class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:   
        totalGas, currGas = 0, 0
        st = 0
        n = len(gas)

        for i in range(n):
            totalGas += gas[i] - cost[i]
            currGas += gas[i] - cost[i]

            if currGas < 0 :
                st = i+1
                currGas = 0

        return st if totalGas >= 0 else -1
