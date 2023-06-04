class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:


        visited=set()

        res=0

        def bfs(node):
            
            q=collections.deque()
            q.append(node)
            visited.add(node)


            while q:

                curNode = q.popleft()

                for x,nei in enumerate(isConnected[curNode]):
                    if nei==1 and x not in visited:
                        visited.add(x)
                        q.append(x)

            return

        for i in range(len(isConnected)):
            print(i,visited)
            if i not in visited:
                bfs(i)
                res=res+1

        return res
