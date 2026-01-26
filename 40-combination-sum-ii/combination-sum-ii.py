class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def dfs(start,s):
            if sum(s)==target:
                res.append(s[::])
                return
            if sum(s)>target:
                return
            if start >=len(candidates):
                return
            s.append(candidates[start])
            dfs(start+1,s)
            s.pop()

            while start+1<len(candidates) and candidates[start+1]==candidates[start]:
                start=start+1

            dfs(start+1,s)

        dfs(0,[])
        return res
            
            

        