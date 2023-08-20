class Solution:
    def evalRPN(self, tokens: List[str]) -> int:


        res=0
        s=[]
        for i in tokens:

            if i in ('+','-','*','/'):
                a=s.pop()
                b=s.pop()
                
                if i=="+":
                    s.append(b+a)
                if i=="-":
                    s.append(b-a)
                if i=="*":
                    s.append(b*a)
                if i=="/":
                    s.append(int(b/a))

            else:
                s.append(int(i))

        return s.pop()
                

        