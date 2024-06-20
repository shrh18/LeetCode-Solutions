class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def traverse(visited, board, i, j, ret, word, k):
            g1,g2,g3,g4 = False,False,False,False
            if board[i][j]==word[k]:
                visited[i][j]=True
                ret = ret+word[k]
                k+=1
                # print(ret)
                if ret == word:
                    return True
                if i+1<len(board) and visited[i+1][j]==False:
                    g1 = traverse(visited, board, i+1, j, ret, word, k)
                if i-1>-1 and visited[i-1][j]==False:
                    g2 = traverse(visited, board, i-1, j, ret, word, k)
                if j+1<len(board[0]) and visited[i][j+1]==False:
                    g3 = traverse(visited, board, i, j+1, ret, word, k)
                if j-1>-1 and visited[i][j-1]==False:
                    g4 = traverse(visited, board, i, j-1, ret, word, k)
            visited[i][j]=False
            return (g1 or g2 or g3 or g4)

        val = False
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    ret = ""
                    val = traverse(visited, board, i, j, ret, word, 0)
                    if val==True:
                        return True
        return val
            