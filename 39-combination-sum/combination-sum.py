class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        

        res=[]

        def dfs(i,cur):

            if sum(cur)==target:
                res.append(cur.copy())
                return
            if sum(cur)>target or i>=len(candidates):
                return
            
            
            cur.append(candidates[i])
            dfs(i,cur)
            cur.pop()
            dfs(i+1,cur)

        dfs(0,[])

        return res