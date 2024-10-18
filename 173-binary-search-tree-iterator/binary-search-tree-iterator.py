# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.s=[]
        
        cur = root

        while cur.left:
            self.s.append(cur)
            cur=cur.left
        
        self.s.append(cur)

    def next(self) -> int:

        top = self.s.pop()
        res=top

        if top.right:
            cur = top.right
            while cur.left:
                self.s.append(cur)
                cur=cur.left 
            self.s.append(cur)
        return res.val
            

    def hasNext(self) -> bool:

        if len(self.s)>0:
            return True

        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()