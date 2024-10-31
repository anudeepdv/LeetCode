class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        minh = []
        maxh = []

        for i in range(k):
            heappush(maxh, -nums[i])
            heappush(minh,-heappop(maxh))
            if len(minh)>len(maxh):
                heappush(maxh,-heappop(minh))

        median = None
        res=[]
        if k%2:
            median = -maxh[0]
        else:
            median = (-maxh[0] +minh[0])/2
        res.append(median)
        print(median)

        hmap = collections.defaultdict(int)

        for i in range(k,len(nums)):
            
            prev = nums[i-k]
            balance=0
            hmap[prev]+=1
            if prev<=median:
                balance-=1
            else:
                balance+=1

            if nums[i]<=median:
                heappush(maxh, -nums[i])
                balance+=1
            else:
                heappush(minh, nums[i])
                balance-=1

            if balance>0:
                heappush(minh, -heappop(maxh))
            elif balance<0:
                heappush(maxh, -heappop(minh))

            while maxh and hmap[-maxh[0]]:
                hmap[-maxh[0]]-=1
                heappop(maxh)

            while minh and hmap[minh[0]]:
                hmap[minh[0]]-=1
                heappop(minh)

            if k%2:
                median = -maxh[0]
            else:
                median = (-maxh[0] +minh[0])/2
            res.append(median)

        return res


            