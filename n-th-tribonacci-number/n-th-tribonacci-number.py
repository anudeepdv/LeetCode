class Solution:
    def tribonacci(self, n: int) -> int:
        
        l=[0]*(100000)
        l[0]=0
        l[1]=1
        l[2]=1
        
        for i in range(3,n+1):
            l[i]=l[i-1]+l[i-2]+l[i-3]

        return l[n]
