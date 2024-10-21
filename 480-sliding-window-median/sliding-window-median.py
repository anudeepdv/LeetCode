class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        maxh = []
        minh = []

        for i in range(k):
            heappush(maxh, -nums[i])
            heappush(minh, -heappop(maxh))

            if len(minh)>len(maxh):
                heappush(maxh, -heappop(minh))
        
        median =None
        res=[]
        if k%2==1:
            median = -maxh[0]
        else:
            median = (-maxh[0]+minh[0])/2
        res.append(median)
        hmap = collections.defaultdict(int)
        for i in range(k,len(nums)):
            prev = nums[i-k]
            hmap[prev]+=1
            balance = -1 if prev<=median else 1

            if nums[i]<=median:
                balance+=1
                heappush(maxh, -nums[i])
            else:
                balance-=1
                heappush(minh, nums[i])
            
            if balance<0:
                heappush(maxh, -heappop(minh))
            elif balance>0:
                heappush(minh, -heappop(maxh))

            while maxh and hmap[-maxh[0]]:
                hmap[-maxh[0]]-=1
                heappop(maxh)

            while minh and hmap[minh[0]]:
                hmap[minh[0]]-=1
                heappop(minh)
                

            if k%2==1:
                median = -maxh[0]
            else:
                median = (-maxh[0]+minh[0])/2
            res.append(median)

        return res
