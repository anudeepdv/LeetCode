class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent=[i for i in range(n+1)]
        rank=[i for i in range(n+1)]

        def find(i):

            while i!=parent[i]:
                parent[i]=parent[parent[i]]
                i=parent[i]

            return i
        
        def union(a,b):

            para=find(a)
            parb = find(b)

            if rank[para]>rank[parb]:
                parent[parb]=para
                rank[para]+=rank[parb]

            else:
                parent[para]=parb
                rank[parb]+=rank[para]

        for a,b in edges:

            para = find(a)
            parb=find(b)

            if para==parb:
                return [a,b]
            else:
                union(a,b)
                      