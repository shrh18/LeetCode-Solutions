# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ret = []

        def rec(node):
            if not node:
                return
            rec(node.left)
            rec(node.right)
            self.ret.append(node.val)

        rec(root)
        return self.ret
        
        