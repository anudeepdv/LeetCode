class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        b=0 
        res=''
        for i in s:

            if i=='(':
                if b>=1:
                    res+=i
                b+=1
            else:
                if b>1:
                    res+=i
                b-=1

        return res
