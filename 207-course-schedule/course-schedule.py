class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = collections.defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)

        vis = set()
        def dfs(node):

            if node in vis:
                return False

            if adj[node]==[]:
                return True

            vis.add(node)

            for nei in adj[node]:
                if not dfs(nei):
                    return False

            vis.remove(node)

            adj[node]=[]
            return True

        

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True