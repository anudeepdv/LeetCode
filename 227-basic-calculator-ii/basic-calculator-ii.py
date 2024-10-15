class Solution:
    def calculate(self, s: str) -> int:
        
        i = 0 
        cur=prev=res=0
        cur_op = "+"

        while i < len(s):

            if s[i].isnumeric():

                while i<len(s) and s[i].isnumeric():
                    cur=cur*10
                    cur+=int(s[i])
                    i+=1

                i-=1
                # print(cur,cur_op)
                if cur_op =="+":
                    res+=cur
                    prev = cur
                    # print(res,"SS")
                    
                elif cur_op =="-":
                    res-=cur
                    prev=-cur
                    
                elif cur_op=="*":
                    # print(prev,cur,res)
                    res=res-prev
                    res+=prev*cur
                    prev=prev*cur
                elif cur_op=="/":
                    # print(prev,cur,res)
                    res=res-prev
                    res+=int(prev/cur)
                    prev=int(prev/cur)

                cur=0
            elif s[i]!=' ':

                cur_op=s[i]

            i+=1

        return res
                