class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        adjList = collections.defaultdict(list)

        for i in range(len(bombs)):
            for j in range(i+1,len(bombs)):
                x1,y1,r1= bombs[i]
                x2,y2,r2= bombs[j]

                d= math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))

                if r1>=d:
                    adjList[i].append(j)
                
                if r2>=d:
                    adjList[j].append(i)

        
        print(adjList)

        def dfs(i,visited):

            if i in visited:
                return
            visited.add(i)

            for nei in adjList[i]:
                dfs(nei,visited)
        
        ret=0

        for i in range(len(bombs)):
            v=set()
            dfs(i,v)
            ret=max(ret,len(v))
        return ret

