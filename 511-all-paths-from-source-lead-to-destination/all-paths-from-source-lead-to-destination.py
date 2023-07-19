class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        visited={}
        adjlist=collections.defaultdict(list)

        for i in edges:
            adjlist[i[0]].append(i[1])

        def dfs(i,dst):
            
            if i in visited:
                return visited[i]
            if len(adjlist[i])==0:
                return i==dst

            visited[i]=False

            for nei in adjlist[i]:
                if(not dfs(nei,dst)):
                    return False

            visited[i]=True

            return True


        return dfs(source,destination)
            
            
