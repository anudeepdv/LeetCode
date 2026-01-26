class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res=[]
        candidates.sort()
        def dfs(start,cur,total):

            
            if total==target:
                res.append(cur.copy())
                return

            if start>=len(candidates) or total>target:
                return

            dfs(start+1,cur+[candidates[start]],total+candidates[start])
            while start+1<len(candidates) and candidates[start]==candidates[start+1]:
                start=start+1

            dfs(start+1,cur,total)
        dfs(0,[],0)
        return res
