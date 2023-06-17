class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        adjList= collections.defaultdict(list)
        n = len(points)
        for i in range(n):

            x1,y1= points[i]

            for j in range(i+1,n):
                x2,y2=points[j]

                d=abs(x1-x2)+abs(y1-y2)

                adjList[i].append((d,j))
                adjList[j].append((d,i))



        h=[]
        heapq.heapify(h)

        heapq.heappush(h,(0,0))
        visited=set()
        res=0
        while len(visited)!=n:
            pop,i=heapq.heappop(h)

            if i in visited:
                continue
            res=res+pop
            visited.add(i)

            for nei, neii in adjList[i]:
                heapq.heappush(h,(nei,neii))

        return res


