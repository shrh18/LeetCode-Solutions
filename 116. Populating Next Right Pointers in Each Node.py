"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        ret = []
        levels = defaultdict(list)
        def bfs(node, level):
            if not node:
                return

            levels[level].append(node)
            bfs(node.left, level+1)
            bfs(node.right, level+1)

            return

        bfs(root, 0)
        for level, nodes in levels.items():
            if len(nodes)==1:
                for node in nodes:
                    node.next = None
            else:
                for i in range(len(nodes)-1):
                    nodes[i].next = nodes[i+1]
                nodes[-1].next = None

        return root