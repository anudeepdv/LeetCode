class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        res=0
        l=0
        sign=1
        while l <len(s) and s[l]==" ":
            l+=1
        if l <len(s) and s[l] in "+-":
            sign=1 if s[l]=='+' else -1
            l+=1

        while l <len(s) and s[l]=='0':
            l+=1
        
        while l<len(s):

            if s[l] not in "0123456789":
                break
            else:
                res=res*10+int(s[l])
            l+=1

        
        resn = 0 if res in('','-','+') else sign*res

        if resn< -2**31:
            return -2**31
        elif resn> 2**31-1:
            return 2**31-1

        return resn
