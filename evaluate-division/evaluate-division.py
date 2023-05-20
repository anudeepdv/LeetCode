class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adjacency_list=collections.defaultdict(list)
        for i in range(len(equations)):
            adjacency_list[equations[i][0]].append([equations[i][1],values[i]])
            adjacency_list[equations[i][1]].append([equations[i][0],1/values[i]])

        print(adjacency_list)

        def bfs(source, target):
            if target not in adjacency_list:
                return -1

            q=collections.deque([(source,1)])
            visited=set()

            while q:
                i= q.popleft()
                if i[0]==target:
                    return i[1]

                for nei in adjacency_list[i[0]]:
                   
                    if nei[0] not in visited:
                        visited.add(nei[0])
                        q.append((nei[0],i[1]*nei[1]))

            return -1



        res=[]
        for i in queries:
            res.append(bfs(i[0],i[1]))

        return res


