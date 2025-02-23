# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        dic = defaultdict(int)
        for i, num in enumerate(inorder):
            dic[num] = i

        def build(il, ir, pl, pr):
            if il>ir or pl>pr:
                return None

            rootVal = postorder[pr]
            root = TreeNode(rootVal)

            leftSubTreeSize = dic[rootVal] - il

            root.left = build(il, dic[rootVal]-1, pl, pl+leftSubTreeSize-1)
            root.right = build(dic[rootVal]+1, ir, pl+leftSubTreeSize, pr-1)

            return root

        return build(0, len(inorder)-1, 0, len(postorder)-1)