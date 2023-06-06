class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adjList= collections.defaultdict(list)

        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        q=collections.deque()
        visited=set()

        q.append((0,-1))
        visited.add(0)

        while q:

            for i in range(len(q)):
            
                a = q.popleft()
                print(a)
                parent,prev =a[0],a[1]

                for nei in adjList[parent]:

                    if nei==prev:
                        continue
                    elif nei in visited:
                        return False
                    else:
                        q.append((nei,parent))
                        visited.add(nei)


        if len(visited)==n:
            return True
        return False

        