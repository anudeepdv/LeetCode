class Solution:
    def simplifyPath(self, path: str) -> str:

        pathList = path.split('/')
        print(pathList)
        stack=[]
        for i in pathList:
            if i == '.' or i =='':
                continue
            elif i =='..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)

        return '/'+'/'.join(stack)