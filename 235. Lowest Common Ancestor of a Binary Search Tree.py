# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = root
        if not root:
            return 0

        def travel(node):
            if not node:
                return None
            
            if (p.val<node.val and node.val<q.val) or (q.val<node.val and node.val<p.val):
                return node

            if p.val<node.val and q.val<node.val:
                return travel(node.left)
            elif p.val>node.val and q.val>node.val:
                return travel(node.right)
            else:
                return node

        return travel(root)

        