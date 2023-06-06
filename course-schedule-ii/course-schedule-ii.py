class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adjList=collections.defaultdict(list)

        for s,d in prerequisites:
            adjList[d].append(s)

        visitedMap={}
        for i in range(numCourses):
            visitedMap[i]=0


        def isCycle(node):

            if visitedMap[node]==2:
                return True
            
            visitedMap[node]=2

            for nei in adjList[node]:
                if visitedMap[nei]!=1:
                    if isCycle(nei):
                        return True
            visitedMap[node]=1

            return False

        for i in range(numCourses):
            if visitedMap[i]==0:
                if isCycle(i):
                    return []

        # If there is no isCycle, we can do a dfs to find the findOrder

        visited=set()

        stack=[]
        def dfs(node):
            
            visited.add(node)
            for nei in adjList[node]:
                if nei not in visited:
                    dfs(nei)

            stack.append(node)
            return


        for i in range(numCourses):
            if i not in visited:
                dfs(i)

        
        return reversed(stack)

        



