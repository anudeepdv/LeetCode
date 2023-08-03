class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:


        res=[]

        def dfs(i,lis):
            # print(lis,k)
            if len(lis)==k:
                print(lis,'BREAK')
                res.append([l for l in lis])
                return
            
            for j in range(i,n+1):
                lis.append(j)
                dfs(j+1,lis)
                lis.pop()

        dfs(1,[])
        return res