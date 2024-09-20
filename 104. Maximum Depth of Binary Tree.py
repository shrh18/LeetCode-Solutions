# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.depth = 0
        if not root:
            return 0
        def traverse(node):
            if not node:
                return 1
            
            self.depth = max(traverse(node.left), traverse(node.right))

            return 1+self.depth

        traverse(root)
        return self.depth
