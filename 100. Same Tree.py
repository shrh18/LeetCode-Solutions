# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ret = True
        def traverse(p,q,ret):

            if p is None and q:
                ret = False
                return ret
            if q is None and p:
                ret = False
                return ret

            if p is None or q is None:
                return ret

            if p.val!=q.val:
                ret = False
                return ret
            
            l = traverse(p.left, q.left, ret)
            r = traverse(p.right, q.right, ret)
            return l and r
        ret = traverse(p, q, ret)
        return ret
