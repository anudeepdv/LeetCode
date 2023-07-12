# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        q=collections.deque()
        if root is None:
            return []
        q.append((root,root.val,[root.val]))
        res=[]
        while q:
            
            for _ in range(len(q)):
                node,val,curList=q.popleft()
                print(node.val,val)
                if node.left is None and node.right is None and val==targetSum:
                    res.append(curList)
                if  node.left:
                    q.append((node.left,val+node.left.val,curList+[node.left.val]))
                if  node.right:
                    q.append((node.right,val+node.right.val,curList+[node.right.val]))



                


        return res