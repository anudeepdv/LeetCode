class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        bc=[0]*n
        ans=[]
        def dfs(i,count):

            if i==len(requests):            
                for i in bc:
                    if i!=0:
                        return
                ans.append(count)
                return
            
            bc[requests[i][0]]=bc[requests[i][0]]-1
            bc[requests[i][1]]=bc[requests[i][1]]+1

            dfs(i+1,count+1)

            bc[requests[i][0]]=bc[requests[i][0]]+1
            bc[requests[i][1]]=bc[requests[i][1]]-1

            dfs(i+1,count)

        dfs(0,0)

        return max(ans)





