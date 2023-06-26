# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:

        q= collections.deque()

        visited =set()

        q.append(root1)
        visited.add(root1)

        visele=set()
        visele.add(root1.val)
        while q:
            
            for i in range(len(q)):
                r = q.popleft()

                if r.left:
                    q.append(r.left)
                    visited.add(r.left)
                    visele.add(r.left.val)

                if r.right:
                    q.append(r.right)
                    visited.add(r.right)
                    visele.add(r.right.val)

        
        q1=collections.deque()
        q1.append(root2)
        visited1 =set()
        visited1.add(root2)

        print(visele)

        while q1:
            
            for i in range(len(q1)):
                r = q1.popleft()

                if target-r.val in visele:
                    return True

                if r.left:
                    q1.append(r.left)
                    visited1.add(r.left)
                    # visele.add(r.left.val)

                if r.right:
                    q1.append(r.right)
                    visited1.add(r.right)
                    # visele.add(r.right.val)


        return False



                


