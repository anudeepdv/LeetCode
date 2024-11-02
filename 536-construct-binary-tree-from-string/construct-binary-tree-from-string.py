# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:

        if not s:
            return

        i = 0
        stack = []

        while i< len(s):

            val = s[i]

            if val =='-':
                i+=1
                cur =0
                while i<len(s) and s[i].isdigit():
                    cur = cur*10 + int(s[i])
                    i+=1

                i-=1
                stack.append(TreeNode(-cur))
            elif s[i].isdigit():
                cur =0
                while i<len(s) and s[i].isdigit():
                    cur = cur*10 + int(s[i])
                    i+=1

                i-=1
                stack.append(TreeNode(cur))

            elif s[i]==')':
                top = stack.pop()
                prev = stack.pop()

                if prev.left is None:
                    prev.left= top
                else:
                    prev.right= top

                stack.append(prev)

            i+=1

        return stack[0]
