class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = [i for i in range(n)]
        used = []
        c=[0]*n
        for start,end in meetings:

            while used and used[0][0]<=start:
                _,room = heapq.heappop(used)
                heapq.heappush(available,room)

            if len(available)==0:
                endTime,room = heapq.heappop(used)
                end = end+(endTime-start)
                heapq.heappush(available,room)
                
            roomNo = heapq.heappop(available)
            heapq.heappush(used,(end,roomNo))
            c[roomNo]+=1

        return c.index(max(c))





        