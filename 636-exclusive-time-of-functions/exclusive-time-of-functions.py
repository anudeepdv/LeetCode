class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        s = collections.deque()

        res = [0 for i in range(n)]
        prev = 0

        for i in range(len(logs)):
            f,status,time = logs[i].split(":")
            time=int(time)

            if status =="start":
                if not s:
                    s.append((int(f),time))
                else:
                    pf = s[-1][0]
                    res[pf]=res[pf]+time-prev
                    prev= time
                    s.append((int(f),time))
            else:

                pf = s.pop()[0]
                res[pf]=res[pf]+time-prev+1
                prev = time+1

        return res
