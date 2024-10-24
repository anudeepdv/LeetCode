"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return
        first =None
        last=None
        def inorder(node):
            nonlocal first
            nonlocal last
            if not node:
                return

            inorder(node.left)

            if not last:
                first = node
            else:
                node.left=last
                last.right=node

            last=node

            inorder(node.right)

        inorder(root)

        first.left= last
        last.right =first

        return first


