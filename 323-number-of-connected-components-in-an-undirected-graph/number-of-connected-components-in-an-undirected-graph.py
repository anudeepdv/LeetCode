class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        
        par = [i for i in range(n)]

        rank = [1 for i in range(n)]

        def find(p1):
            
            res=p1
            while res!=par[res]:
                res = par[res]

            return res

        def union(p1,p2):

            par1 = find(p1)
            par2 = find(p2)

            if par1==par2:
                return 0 

            if rank[par1]>rank[par2]:
                par[par2]=par[par1]
                rank[par1]+=rank[par2]
            else:
                par[par1]=par[par2]
                rank[par2]+=rank[par1]

            return 1

        tot = n 

        for n1,n2 in edges:
            if union(n1,n2):
                tot-=1

        return tot 