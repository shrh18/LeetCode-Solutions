# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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

        return list(levels.values())

