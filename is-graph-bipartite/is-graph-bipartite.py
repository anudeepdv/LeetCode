class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        visited=[0]*len(graph)
       
        def bfs(k):
            if visited[k]:
                return True

            q = collections.deque([k])
            visited[k]=-1

            while q:
                i = q.popleft()

                for n in graph[i]:
                    if visited[n]==0:
                        visited[n]=visited[i]*-1
                        q.append(n)
                    elif visited[n]==visited[i]:
                        return False


            return True


        for i in range(len(graph)):
            print(visited)
            if not bfs(i):
                return False

        return True


                

            



