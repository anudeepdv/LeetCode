class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []

        for a,b in points:
            if len(h)<k:
                dis = -math.sqrt(a**2+b**2)
                heappush(h, (dis,a,b))

            else:
                dis = -math.sqrt(a**2+b**2)
                if -dis<-h[0][0]:
                    heappop(h)
                    heappush(h, (dis,a,b))

        res=[]
        for i in h:
            res.append([i[1],i[2]])
        return res