class Solution:
    def hammingWeight(self, n: int) -> int:

        one=0

        while n :
        
            print(n,n%2)
            if n%2==1:
                one=one+1
            n=n>>1

        return one

