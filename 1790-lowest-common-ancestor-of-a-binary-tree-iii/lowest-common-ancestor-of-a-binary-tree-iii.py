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
        pcopy=p
        qcopy=q

        while pcopy!=qcopy:
            pcopy = pcopy.parent if pcopy else q
            qcopy = qcopy.parent if qcopy else p

        return pcopy