# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ret = True

        def rec(node, level):
            if not node:
                print(level-1)
                return level
            
            l = rec(node.left, level+1)
            r = rec(node.right, level+1)

            if abs(l-r)>1:
                self.ret = False

            return max(l, r)

        rec(root, 0)
        return self.ret