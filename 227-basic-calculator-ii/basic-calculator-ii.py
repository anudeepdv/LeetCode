class Solution:
    def calculate(self, s: str) -> int:
        
        cur=prev=res=0

        cur_op='+'

        i=0

        while i<len(s):
            if s[i].isnumeric():
                while i<len(s) and s[i].isnumeric():
                    cur=cur*10+int(s[i])
                    i+=1
                i=i-1

                if cur_op =="+":
                    res=res+cur
                    prev=cur

                elif cur_op=='-':
                    res=res-cur
                    prev=-cur
                elif cur_op =="*":
                    res=res-prev
                    res+=prev*cur
                    prev = prev*cur
                elif cur_op =="/":
                    res=res-prev
                    res+=int(prev/cur)
                    prev = int(prev/cur)

                cur=0

            elif s[i]!=' ':
                cur_op=s[i]

            i+=1

        return res

