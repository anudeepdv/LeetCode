class Solution:
    def isHappy(self, n: int) -> bool:
        
        v=set()

        t = n
        while True:

            cur=str(t)
            print(cur)
            res=0
            for i in cur:
                res+=int(i)*int(i)
            
            if res==1:
                return True
            elif res in v:
                return False

            v.add(res)
            t=res