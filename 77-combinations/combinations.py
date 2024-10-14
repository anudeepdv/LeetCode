class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res=[]

        def dfs(cur,l):
            print(l)
            if len(l)==k:
                res.append([j for j in l])
                return

            for i in range(cur,n+1):
                dfs(i+1,l+[i])
                


        dfs(1,[])
        return res