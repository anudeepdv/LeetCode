class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res=[]
        s = []

        def rec(l,r):

            if l==r==n:
                res.append("".join(s))
                return

            if r<l:
                s.append(')')
                rec(l,r+1)
                s.pop()
            
            if l<n:
                s.append('(')
                rec(l+1,r)
                s.pop()

        rec(0,0)

        return res
        