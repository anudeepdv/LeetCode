class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        tickets.sort()
        adjList = collections.defaultdict(list)
        for src, dest in tickets:
            adjList[src].append(dest)

        res = ["JFK"]

        def dfs(v):

            if len(res)==len(tickets)+1:
                return True
            
            if src not in adjList:
                return False

            temp = adjList[v]

            for i,vert in enumerate(temp):
                res.append(vert)
                adjList[v].pop(i)

                if dfs(vert):
                    return True
                
                res.pop()
                adjList[v].insert(i,vert)

        
        dfs("JFK")

        return res

