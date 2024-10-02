"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        hm = {}
        def travel(oldNode):
            if oldNode in hm:
                return hm[oldNode]
            nn = Node(oldNode.val)
            hm[oldNode] = nn

            for nei in oldNode.neighbors:
                nn.neighbors.append(travel(nei))

            return nn
        
        return travel(node)

        