class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        R, C = len(matrix), len(matrix[0])
        visited = [[False]*C for i in range(R)]
        ret = []
        def right(r,c):
            while r<R and c<C and not visited[r][c]:
                ret.append(matrix[r][c])
                visited[r][c] = True
                if c<C-1 and not visited[r][c+1]:
                    c+=1
            if r+1<R and not visited[r+1][c]:
                down(r+1,c)
        def down(r,c):
            while r<R and c<C and not visited[r][c]:
                ret.append(matrix[r][c])
                visited[r][c] = True
                if r<R-1 and not visited[r+1][c]:
                    r+=1
            if c-1>=0 and not visited[r][c-1]:
                left(r,c-1)
        def left(r,c):
            while r<R and c<C and not visited[r][c]:
                ret.append(matrix[r][c])
                visited[r][c] = True
                if c>0 and not visited[r][c-1]:
                    c-=1
            if r-1>=0 and not visited[r-1][c]:
                up(r-1,c)
        def up(r,c):
            while r<R and c<C and not visited[r][c]:
                ret.append(matrix[r][c])
                visited[r][c] = True
                if r>0 and not visited[r-1][c]:
                    r-=1
            if c+1<C and not visited[r][c+1]:
                right(r,c+1)
        right(0,0)
        return ret