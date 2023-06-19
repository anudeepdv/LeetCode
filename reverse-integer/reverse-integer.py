class Solution:
    def reverse(self, x: int) -> int:
        
        if x==0:
            return 0
        num=[]

        a=abs(x)

        while a!=0:
            num.append(str(a%10))
            a=a//10
        num= int(''.join(num))
  
        num= -num if x<0 else num

        if num<=(-2)**31 or num>= 2**31-1:
            return 0
        return num