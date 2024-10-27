class Solution:
    def calculate(self, s: str) -> int:
        
        res=0
        cur=0
        sign =1
        q=[]

        for i in s:
            if i.isdigit():
                cur=cur*10 +int(i)

            elif i in "+-":
                
                res=res+sign*cur
                cur=0
                sign= 1 if i=="+" else -1
            elif i =='(':
                q.append(res)
                q.append(sign)
                sign=1
                cur=0
                res=0
            elif i==')':
                res=res+cur*sign
                res=res*q.pop()
                res=res+q.pop()
                cur=0
                sign=1

        return res+cur*sign
                