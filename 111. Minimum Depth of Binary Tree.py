# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.level = 0
        ret = []
        def dfs(node, level):
            if not node:
                return 
            level+=1
            if node.left:
                dfs(node.left, level)
            if node.right:
                dfs(node.right, level)
            if not node.left and not node.right:
                ret.append(level)
        dfs(root, 0)
        ret = [i for i in ret if i is not None]
        return min(ret)

        