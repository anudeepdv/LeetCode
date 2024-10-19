# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        lvl = collections.defaultdict(list)

        res= True
        def dfs(node,i):
            nonlocal res

            if not node:
                return
            
            if i%2==0:
                if node.val%2 ==0:
                    res=False
                    return False
                if i in lvl:
                    if node.val<=lvl[i][-1]:
                        res=False
                        return False
                    else:
                        lvl[i].append(node.val)
                else:
                    lvl[i].append(node.val)
            else:
                if node.val%2 ==1:
                    res=False
                    return False
                if i in lvl:
                    if  node.val>=lvl[i][-1]:
                        res=False
                        return False
                    else:
                        lvl[i].append(node.val)
                else:
                    lvl[i].append(node.val)

            dfs(node.left,i+1)
            dfs(node.right,i+1)

        dfs(root,0)
        print(lvl)
        return res
