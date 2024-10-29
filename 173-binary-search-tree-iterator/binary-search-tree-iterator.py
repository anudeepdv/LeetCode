# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.s = deque()

        cur =root
        while cur:
            self.s.append(cur)
            cur=cur.left

    def next(self) -> int:
        ret = self.s.pop()

        cur = ret.right

        while cur:
            self.s.append(cur)
            cur=cur.left   
        return ret.val

    def hasNext(self) -> bool:
        return True if len(self.s)>0 else False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()