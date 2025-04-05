# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if root and root.left is None and root.right is None:
        #     return root

        def dfs(node):
            if not node:
                return (0, node)

            ld, la = dfs(node.left)
            rd, ra = dfs(node.right)

            if ld > rd:
                return (ld+1, la)
            elif rd > ld:
                return (rd+1, ra)
            else:
                return (ld+1, node)

        return dfs(root)[1]
            