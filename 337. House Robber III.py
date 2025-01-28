# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # [ wr, nr]
        def dfs(node):
            if not node:
                return (0, 0)
            (l0, l1) = dfs(node.left)
            (l2, l3) = dfs(node.right)
            return (node.val+l1+l3, max(l0, l1) + max(l2, l3))

        (wr, nr) = dfs(root)
        return max(wr, nr)