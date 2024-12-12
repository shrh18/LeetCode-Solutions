class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # ls = []
        # for nums in matrix:
        #     for num in nums:
        #         ls.append(num)
        # heapq.heapify(ls)
        # while k>1:
        #     heapq.heappop(ls)
        #     k-=1
        # return heapq.heappop(ls)

        # Approach 2. Add parent then its children and then pop them
        if not matrix or k<1: return
        ss = set() # keeps tracked of visited or done
        ss.add((0,0))
        heap = [(matrix[0][0], 0, 0)]

        while k>1:
            top = heapq.heappop(heap)
            row, col = top[1], top[2]

            if row+1<len(matrix) and (row+1, col) not in ss:
                heapq.heappush(heap, (matrix[row+1][col], row+1, col))
                ss.add((row+1, col))
            if col+1<len(matrix[0]) and (row, col+1) not in ss:
                heapq.heappush(heap, (matrix[row][col+1], row, col+1))
                ss.add((row, col+1))
            k-=1

        return heap[0][0]

        