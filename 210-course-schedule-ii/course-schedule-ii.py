class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = collections.defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)

        vis = set()
        done=set()
        out=[]
        def dfs(node):

            if node in vis:
                return False

            if node in done: 
                return True

            vis.add(node)

            for nei in adj[node]:
                if not dfs(nei):
                    return False

            vis.remove(node)

            done.add(node)
            out.append(node)
            return True

        

        for i in range(numCourses):
            if not dfs(i):
                return []

        return out