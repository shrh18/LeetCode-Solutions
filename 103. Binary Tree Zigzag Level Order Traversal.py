# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        levels = defaultdict(list)
        def bfs(node, level):
            if not node:
                return

            levels[level].append(node.val)
            bfs(node.left, level+1)
            bfs(node.right, level+1)

            return

        bfs(root, 0)
        print(levels)
        ll = list(levels.values())
        for i in range(len(ll)):
            if i%2:
                n = len(ll[i])
                for j in range(n//2):
                    ll[i][j], ll[i][n-j-1] = ll[i][n-j-1], ll[i][j]

        return ll