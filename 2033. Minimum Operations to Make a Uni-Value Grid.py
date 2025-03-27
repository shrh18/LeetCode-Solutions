class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        elem = []
        mm = grid[0][0] % x
        for row in grid:
            for num in row:
                if num%x != mm:
                    return -1
                elem.append(num)
        elem.sort()
        mid = elem[len(elem) // 2]
        
        ops = sum(abs(num-mid) // x for num in elem)

        return ops