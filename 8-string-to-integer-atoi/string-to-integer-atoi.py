class Solution:
    def myAtoi(self, s: str) -> int:
        
        res=''
        for i in range(len(s)):
            val = s[i]

            if val==' ' and res=='':
                continue
            elif res=='' and val in ['+','-']:
               
                res+=val+'0'

            elif val in "0123456789":
                res+=val
            else:
                break
        print(res)
        if res=='':
            return 0
        

        if int(res)< -2**31:
            return -2**31
        elif int(res)>2**31-1:
            return 2**31-1

        return int(res)


            