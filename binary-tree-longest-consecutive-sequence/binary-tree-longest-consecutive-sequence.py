# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        q=collections.deque()
        q.append((root,1))
        res=1
        while q:
            for _ in range(len(q)):
               
                ele,val=q.popleft()

                if ele.left:
                    if ele.left.val==ele.val+1:
                        q.append(( ele.left,val+1))
                        res=max(res,val+1)
                    else:
                         q.append(( ele.left,1))

                if ele.right:
                    if ele.right.val==ele.val+1:
                        q.append(( ele.right,val+1))
                        res=max(res,val+1)
                    else:
                         q.append(( ele.right,1))


        return res
                