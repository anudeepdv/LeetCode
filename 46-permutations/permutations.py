class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        res=[]

        def dfs(comb,cur):
            print(comb)
            if len(comb)==len(nums):
                res.append(comb.copy())
                return

            for i in range(len(cur)):
                dfs(comb+[cur[i]], cur[:i]+cur[i+1:])

        dfs([],nums)
        return res