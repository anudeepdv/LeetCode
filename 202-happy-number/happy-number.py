class Solution:
    def isHappy(self, n: int) -> bool:
        
        v=set()

        while True:

            t=0
            for i in str(n):
                t+=int(i)*int(i)
            print(t)
            if t==1:
                return True
            if t in v:
                return False
            v.add(t)
            n=t