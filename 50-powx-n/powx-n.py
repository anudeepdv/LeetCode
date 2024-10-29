class Solution:
    
    def myPow(self, x: float, n: int) -> float:
        

        def help(x,n):
            if n==0:
                return 1
            if n==1:
                return x

            a= help(x,n//2)

            if n%2==1:
                return a*a*x
            return a*a


        a = help(x, abs(n))

        return a if n>=0 else 1/a
    