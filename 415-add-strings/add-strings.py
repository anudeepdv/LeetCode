class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        i = len(num1)-1
        j = len(num2)-1

        c=0
        res = collections.deque()
        while i>=0 or j>=0:

            v1 = 0 if i<0 else int(num1[i])
            v2 = 0  if j<0 else int(num2[j])
            val = v1+v2 +c

            c=val//10
            val = val%10
            res.appendleft(str(val))
            i-=1
            j-=1

        if c:
            res.appendleft(str(c))

        return ''.join(res)
        

