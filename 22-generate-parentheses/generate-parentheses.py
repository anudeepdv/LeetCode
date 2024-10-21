class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res=[]
        

        def rec(l,r,s):
            if l==r==n:
                res.append(s)

            if l<n:
                rec(l+1,r,s+'(')
            
            if r<l:
                rec(l,r+1,s+')')

        rec(0,0,"")
        return res
