class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=collections.deque()
        r=[]
        
        for i,val in enumerate(s):
            if val ==')' and stack:
                stack.pop()
            elif val== ')':
                r.append(i)
            elif val=='(':
                stack.append(i)

        res =''

        for i,val in enumerate(s):
            if i not in stack and i not in r:
                res+=val

        return res