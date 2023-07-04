class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = collections.defaultdict(list)

        for s,d in  prerequisites:
            adjList[s].append(d)

        visisted={}

        for i in range(numCourses):
            visisted[i]=0

        def isCycle(node):

            if visisted[node]==2:
                return True

            visisted[node]=2

            for nei in adjList[node]:
                if visisted[nei]!=1:
                    if isCycle(nei):
                        return True

            visisted[node]=1
            return False

        for i in range(numCourses):
            if visisted[i]==0:
                if isCycle(i):
                    return False

        return True
