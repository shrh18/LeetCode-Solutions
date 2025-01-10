class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.eow = True

    def prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return node

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        rows, cols = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)

        result = set()
        
        def dfs(x, y, node, currWord):
            if node.eow:
                result.add(currWord)

            char, board[x][y] = board[x][y], "#"

            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x+dx, y+dy
                if 0<=nx<rows and 0<=ny<cols and board[nx][ny] != "#":
                    nextChar = board[nx][ny]
                    if nextChar in node.children:
                        dfs(nx, ny, node.children[nextChar], currWord+nextChar)
            board[x][y] = char

        for i in range(rows):
            for j in range(cols):
                char = board[i][j]
                if char in trie.root.children:
                    dfs(i, j, trie.root.children[char], char)

        return list(result)
        


