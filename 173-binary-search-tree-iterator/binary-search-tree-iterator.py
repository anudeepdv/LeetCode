# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        self.q = deque()

        cur  = root
        while cur:
            self.q.append(cur)
            cur =cur.left
        

    def next(self) -> int:

        pop  = self.q.pop()

        cur = pop.right
        while cur:
            self.q.append(cur)
            cur=cur.left

        return pop.val        

    def hasNext(self) -> bool:
        if len(self.q)>0:
            return True

        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()