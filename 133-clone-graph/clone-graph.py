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
        d= {}
        vis= set()
        def dfs(node):
            if not node:
                return None
            if node in vis:
                return None
            
            if node not in d:
                d[node]=Node(node.val, [])

            vis.add(node)

            for nei in node.neighbors:
                if nei not in d:
                    d[nei]=Node(nei.val, [])
                d[node].neighbors.append(d[nei])
                dfs(nei)

        dfs(node)
        return d[node]
