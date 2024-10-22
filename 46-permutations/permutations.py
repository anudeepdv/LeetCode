class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res=[]

        def dfs(i,l,l1):
            print(l,l1)
            if i == len(nums):
                res.append([k for k in l])
                return

            for j in range(len(l1)):
                dfs(i+1,l+[l1[j]],l1[:j]+l1[j+1:])

        dfs(0,[],nums)
        return res