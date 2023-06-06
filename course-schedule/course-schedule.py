class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjList=collections.defaultdict(list)

        for s,d in prerequisites:
            adjList[s].append(d)

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
                    return False

        return True

        
