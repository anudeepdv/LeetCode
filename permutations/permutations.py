class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n=len(nums)
        res=[]
        def dfs(comb,path):
            if len(path)==n:
                res.append(path)

            for i in range(len(comb)):
                dfs(comb[:i]+comb[i+1:],path+[comb[i]])

        dfs(nums,[])
        return res



