class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:

        jobs.sort(reverse=True)
        buckets = [0]*k

        n=len(jobs)

        def dfs(i):
            ans =float('inf')
            vis=set()
            if i==n:
                return max(buckets)

            for j in range(k):
                if buckets[j] in vis :
                    continue
                vis.add(buckets[j])
                buckets[j]+=jobs[i]
                if max(buckets)<ans:
                    ans = min(ans,dfs(i+1))
                buckets[j]-=jobs[i]

            return ans

        return dfs(0)

