class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:

        res=[]
        for i in range(len(nums)):
            res.append((nums[i],cost[i]))

        res.sort()
      

        l=min(nums)
        r=max(nums)
        ind=0

        def cal(m):
            cost=0
            for i in res:
                cost=  cost+ abs(m-i[0])*i[1]
            return cost

        while l<=r:

            m= (l+r)//2
            
            if(cal(m)<cal(m+1)):
                ind =m
                r=m-1

            else:
                l=m+1

        return cal(ind)
