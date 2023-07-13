class Solution:
    def parseTernary(self, expression: str) -> str:
    
        i=len(expression)-1

        s=collections.deque()
        while i>0:

            if expression[i]=='?':
                one=s.pop()
                two=s.pop()

                exp =one if expression[i-1] =='T'  else two
                s.append(exp)
                i=i-2
            elif expression[i]==':':
                i=i-1
                continue
            else:
                s.append(expression[i])
                i=i-1

        return s.pop()

