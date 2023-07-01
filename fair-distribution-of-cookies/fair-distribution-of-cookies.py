class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int: 

        buckets = [0]*k
        n=len(cookies)
        vals=[]
        def dfs(i):
            ans=float('inf')
            vis=set()
            if i==n:
                return max(buckets)
            

            for j in range(k):
                if buckets[j] in vis:
                    continue
                vis.add(buckets[j])
                buckets[j]+=cookies[i]
                ans=min(ans,dfs(i+1))
                buckets[j]-=cookies[i]

            return ans

        return dfs(0)

