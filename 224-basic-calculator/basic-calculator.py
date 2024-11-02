class Solution:
    def calculate(self, s: str) -> int:
        
        res=0
        cur=0
        sign =1
        q=[]

        i =0 

        while i < len(s):

            if s[i].isdigit():
                while i < len(s) and  s[i].isdigit():
                    cur = cur*10 +int(s[i])
                    i+=1
                i-=1
                
            if s[i] != " ":
                if s[i]=='(':
                    q.append(res)
                    q.append(sign)
                    res=0
                    sign=1
                    cur =0

                elif s[i]==')':
                    res = res + cur*sign
                    res= res*q.pop()
                    res=res+q.pop()
                    cur = 0
                    sign =1

                elif s[i] in "+-":
                    res=res+cur*sign
                    sign = 1 if s[i]=='+' else -1
                    cur=0

                
            
            i+=1


        return res +cur*sign
