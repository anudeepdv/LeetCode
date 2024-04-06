class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=collections.deque()
        r=[]
        for  index,i in enumerate(s):
            if i ==')' and stack:
                stack.pop()
            elif i==')':
                r.append(index)
            elif i=='(':
                stack.append(index)

        # print(r,stack)

        res=r+list(stack)
        print(res)

        output=""
        for i,val in enumerate(s):
            if i not in res:
                output+=val
        return output

        return ""
        