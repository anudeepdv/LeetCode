# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        ans =1

        q=collections.deque()
        q.append((root,root.val))
        
        while q:

            pop,curMax = q.popleft()

            if pop.left:
                left = pop.left
                if left.val>=curMax:
                    ans+=1
                newMax= max(curMax,left.val)
                q.append((left,newMax))

            if pop.right:
                right = pop.right
                if right.val>=curMax:
                    ans+=1
                newMax= max(curMax,right.val)
                q.append((right,newMax))

        return ans