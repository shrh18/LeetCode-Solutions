# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        self.count = 0    
        dic = defaultdict(list)

        def rec(node, level):
            q = deque([(node, level)])

            while q:
                n, l = q.popleft()
                dic[l].append(n.val)
                if n.left and n.right:
                    q.append((n.left, l+1))
                    q.append((n.right, l+1))
                elif n.left and not n.right:
                    q.append((n.left, l+1))
                elif not n.left and n.right:
                    q.append((n.right, l+1))

        def ms(arr):
            ss = sorted(arr)
            d = defaultdict(int)
            for i, n in enumerate(arr):
                d[n] = i

            for i in range(len(ss)):
                if arr[i] != ss[i]:
                    orig = i
                    rep = d[ss[i]]

                    arr[orig], arr[rep] = arr[rep], arr[orig]
                    d[arr[orig]] = orig
                    d[arr[rep]] = rep
                    
                    self.count += 1

        rec(root, 0)

        for v in list(dic.values()):
            if len(v)>1:
                ms(v)
        return self.count