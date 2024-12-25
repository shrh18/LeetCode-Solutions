# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def checkPal(arr):
            l,r = 0, len(arr)-1
            while l<r:
                if arr[l]!=arr[r]:
                    return False
                l+=1
                r-=1
            return True
        
        ls = defaultdict(list)

        def rec(node, level):
            if not node:
                ls[level].append(-101)
                return

            ls[level].append(node.val)
            rec(node.left, level+1)
            rec(node.right, level+1)

        rec(root, 0)
        print(ls)
        for k, v in ls.items():
            if not checkPal(v):
                return False
        return True

        