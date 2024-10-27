class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        q = collections.deque()
        inv = collections.deque()

        for i,val in enumerate(s):
            if q and val==')':
                q.pop()
            elif val==')':
                inv.append(i)
            elif val =='(':
                q.append(i)

        res=""
        for i in range(len(s)):
            if not(i in q or i in inv):
                res+=s[i]
        return res

