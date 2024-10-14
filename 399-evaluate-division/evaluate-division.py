class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adj = collections.defaultdict(list)

        for  i in range(len(equations)):
            s,d = equations[i]
            val = values[i]

            adj[s].append((d,val))
            adj[d].append((s,1/val))

        print(adj)

        def dfs(node,dst,vis,res):
            nonlocal val
            if node == dst:
                val = res
                return res
            
            if node in vis:
                return
            

            vis.add(node)

            for nei,v in adj[node]:

                if nei not in vis:
                    dfs(nei,dst,vis,res*v)

            


        res=[]
        for s,d in queries:
            vis=set()
            val=-1
            if s not in adj or d not in adj:
                res.append(-1)
            else:
                dfs(s,d,vis,1)
                res.append(val)

        return res