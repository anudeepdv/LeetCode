class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        res=[]
        def dfs(i , c):

            if i == n:
                print(c)
                res.append([k for k in c])
                return

            c.append(nums[i])
            
            dfs(i+1,c)
            c.pop()
            dfs(i+1,c)

        dfs(0,[])

        return res                