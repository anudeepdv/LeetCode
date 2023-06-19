class Solution:
    def simplifyPath(self, path: str) -> str:

        pathList = path.split('/')

        stack=[]
        for i in pathList:
            if i=='..' and stack:
                stack.pop()
            elif i=='.' or i=='':
                continue
            elif i!='..':
                stack.append(i)

        print(stack)
        return '/'+'/'.join(stack)
