# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        vals = []
        levels = []
        level = 0
        def dfs(node, level):
            if not node:
                return

            if level not in levels:
                vals.append(node.val)
                levels.append(level)
            level+=1
            dfs(node.right, level)
            dfs(node.left, level)

        dfs(root, level)
        return vals