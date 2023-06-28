class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        adjList =collections.defaultdict(list)

        for i in range(len(edges)):
            s,d = edges[i]
            p=succProb[i]

            adjList[s].append((d,p))
            adjList[d].append((s,p))



        res=[0.0]*n
        q= collections.deque()

        q.append(start)
        res[start]=1.0
        while q:

            pop = q.popleft()
            
            for nei,prob in adjList[pop]:
                new = res[pop]*prob

                if new>res[nei]:
                    res[nei]=new
                    q.append(nei)

        return res[end]