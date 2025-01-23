class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        r, c = len(mat), len(mat[0])
        rows, cols = [0]*r, [0]*c

        dic = defaultdict(tuple)
        for i in range(r):
            for j in range(c):
                dic[mat[i][j]] = (i, j)

        for i in range(len(arr)):
            x, y = dic[arr[i]]
            rows[x] += 1
            cols[y] += 1

            if rows[x]==c or cols[y]==r:
                return i