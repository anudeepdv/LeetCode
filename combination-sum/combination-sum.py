class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res=[]

        arr=[]
        def dfs(i,curSum,arr):
            
            if i >=len(candidates):
                return
            
            if curSum>target:
                return
            
            if curSum==target:
                print(curSum)
                res.append(arr.copy())
                return

            arr.append(candidates[i])
            print(arr,curSum+candidates[i])
            dfs(i,curSum+candidates[i],arr)
            arr.pop()
            dfs(i+1,curSum,arr)

        dfs(0,0,arr)
        return res