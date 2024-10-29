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

        self.first = None
        self.last = None

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)

            if not self.last:
                self.first = node
            else:
                node.left=self.last
                self.last.right = node

            self.last=node

            inorder(node.right)

        inorder(root)

        self.first.left=self.last
        self.last.right = self.first

        return self.first

