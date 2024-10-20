class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        q=deque()

        prev = 0

        res= [0]*n
        for  i in range(len(logs)):
            func,state,time = logs[i].split(":")
            func = int(func)
            time = int(time)
            print(time)
            if state =="start":
                if q:
                    prevf = q[-1]
                    res[prevf]+=time-prev
                    print(res)
                    prev=time
                    q.append(func)

                else:
                    q.append(func)

            else:
                prevf = q.pop()
                res[prevf]+=time-prev+1
                prev=time+1
                print(res)

        return res

