class Solution:
    def calculate(self, s: str) -> int:
        
        i = 0

        q= []

        cur = 0

        sign = "+"

        while i < len(s):

            if s[i].isdigit():
                while i < len(s) and s[i].isdigit():
                    cur = cur * 10 + int(s[i])
                    i+=1
                i-=1

            if s[i] in "+-/*" or i==len(s)-1:
                if sign=="+":
                    q.append(cur)
                elif sign=="-":
                    q.append(-cur)
                elif sign=="*":
                    a=q.pop()
                    q.append(cur*a)
                elif sign=="/":
                    a=q.pop()
                    q.append(int(a/cur))

                sign=s[i]
                cur=0
            i+=1
            
        print(q)
        res=0
        for i in q:
            res+=i

        return res


