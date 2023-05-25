# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q =collections.deque()
        res=[root.val]
        q.append(root)

        while q:
            val=None
            rightfound=False
            for i in range(len(q)):
               
                node = q.popleft()

             

                if node.left:
                    q.append(node.left)
                    val = node.left.val
                if node.right:
                    q.append(node.right)
                    val = node.right.val
                  
                
                print(val)
            if val is not None:
                res.append(val)

        return res


            
        
        return res