class Solution:
    def calculate(self, s: str) -> int:

        res, cur = 0,0 
        stack = []
        sign =1

        for i in s:
            if i.isdigit():
                cur = cur*10 + int(i)
            elif i in ["+","-"]:
                res+=cur*sign
                cur =0
                sign = 1 if i=='+'else -1
            elif i =='(':
                stack.append(res)  
                stack.append(sign)    
                sign=1
                res=0
                # cur=0
            elif i == ')'  :
                res += cur*sign
                res*=stack.pop()
                res+= stack.pop()
                # sign =1
                cur =0

        return res+ sign*cur