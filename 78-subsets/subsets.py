class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        def dfs(i,l):
            
            if i ==len(nums):
                res.append([k for k in l])
                return

            dfs(i+1,l+[nums[i]])
            dfs(i+1,l)

            return 

        dfs(0,[])
        return res
