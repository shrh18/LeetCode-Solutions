from typing import List

# Brute Force Solution with Time Complexity O(n^2)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        for i in range(0, len(temperatures)-1):
            k=1
            while k+i<(len(temperatures)):
                if temperatures[k+i]>temperatures[i]:
                    answer[i] = k
                    break
                else:
                    k = k+1
        print(answer)
        return answer

# Dynamic Programming Solution with Time Complexity O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prevIndex = stack.pop()
                answer[prevIndex] = i-prevIndex
            stack.append(i)
        print(answer)
        return answer