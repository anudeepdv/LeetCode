class Solution:
    def calculate(self, s: str) -> int:
        
        q = []

        i = 0

        cur = 0

        sign = '+'

        while i<len(s):
            if s[i].isdigit():
                while i<len(s) and s[i].isdigit():
                    cur=cur*10+int(s[i])
                    i+=1
                i-=1
            if s[i] in "+-/*" or i==len(s)-1:
                if sign == '+':
                    q.append(cur)
                    cur=0
                    sign=1

                elif sign=='-':
                    q.append(-cur)
                    cur=0
                    sign=-1

                elif sign=='*':
                    res=cur*q.pop() 
                    q.append(res)
                    cur=0

                elif sign=='/':
                    res=int(q.pop()/cur)
                    q.append(res)
                    cur=0

                sign=s[i]
            i+=1

    

        # print(q)
        res=0

        for i in q:
            res+=i

        return res



