# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        q=deque()
        q.append(root)
        lvl=deque()
        while q:
            lvlsum =0
            for _ in range(len(q)):
                node = q.popleft()
                lvlsum+=node.val

                if node.left:
                    q.append(node.left)  
                if node.right:
                    q.append(node.right)

            lvl.append(lvlsum) 

        print(lvl)

        q=deque()
        q.append(root)
        i=1
        lvl.append(0)
        while q:
            
            for _ in range(len(q)):

                node = q.popleft()

                cursum=0
                if node.left:
                    cursum+=node.left.val

                if node.right:
                    cursum+=node.right.val
                print(lvl[i],cursum,node.val)
                if node.left:
                    node.left.val= lvl[i]-cursum
                    q.append(node.left)  
                if node.right:
                    node.right.val= lvl[i]-cursum
                    q.append(node.right)

            i+=1
        root.val=0
        return root

                
                
                
                              

            
        