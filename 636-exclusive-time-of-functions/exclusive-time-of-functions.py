class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        q=deque()

        prev = 0

        res= [0]*n
        for  i in range(len(logs)):
            func,state,time = logs[i].split(":")
            func = int(func)
            time = int(time)
            if state=="start":
                if q:
                    pf = q[-1]
                    res[pf]+=time-prev
                    prev=time
                    q.append(func)
                else:
                    q.append(func)
                    

            elif state=="end":
                
                pf = q.pop()
                res[pf]+=time-prev+1
                prev=time+1

        return res