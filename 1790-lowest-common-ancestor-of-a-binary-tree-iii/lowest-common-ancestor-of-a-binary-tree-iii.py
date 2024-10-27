"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        pcopy = p 
        qcopy= q

        while pcopy!=qcopy:
            pcopy = pcopy.parent if pcopy.parent is not None else q
            qcopy = qcopy.parent if qcopy.parent is not None else p

        return pcopy
