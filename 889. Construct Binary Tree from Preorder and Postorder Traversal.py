# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def build(preorder, postorder):

            if not preorder:
                return None

            root = TreeNode(preorder[0])
            if len(preorder) == 1:
                return root

            lrv = preorder[1]
            lss = postorder.index(lrv) + 1  

            root.left = build(preorder[1:lss+1], postorder[:lss])
            root.right = build(preorder[lss+1:], postorder[lss:-1])

            return root

        return build(preorder, postorder)

