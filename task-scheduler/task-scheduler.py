class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        tasks = collections.Counter(tasks)

        h = [ -h for h in tasks.values()]

        heapq.heapify(h)
        print(h)

        q =collections.deque()

        time =0

        while h or q:
            time=time+1
            if h:
                t  = 1 + heapq.heappop(h)
                if t:
                    q.append((t,time+n))
            
            if q and q[0][1]==time:
                ele = q.popleft()
                heapq.heappush(h,ele[0])

        return time
                
