class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res=[]
        n = len(candidates)
        def dfs(i,l):

            if i>=n:
                return

            if sum(l)==target:
                print(i)
                res.append([k for k in l])
                return

            if sum(l)>target:
                # res.app?end([k for k in l])
                return

            

            
            
            dfs(i,l+[candidates[i]])
            dfs(i+1,l)

        dfs(0,[])
        return res
