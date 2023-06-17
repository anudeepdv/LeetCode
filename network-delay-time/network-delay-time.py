class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:


        adjList=collections.defaultdict(list)
        for s,d,dis in times:
            adjList[s].append([d,dis])

        h=[(0,k)]
        heapq.heapify(h)

        visited=set()
        res=0
        while h:
            # print(res,h)
            pop,i =heapq.heappop(h)
            
            if i in visited:
                continue

            visited.add(i)
            res=max(res,pop)
            for nei,dis in adjList[i]:
                heapq.heappush(h,(dis+pop,nei))

        # print(res,visited)
        return res if len(visited)==n else -1


