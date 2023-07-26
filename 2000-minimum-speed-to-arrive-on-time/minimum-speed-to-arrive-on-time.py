class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        l =1
        r= 10**7
        res=-1
        while l<=r:

            m = (l+r)//2
            time=0
            for  i in range(0,len(dist)-1):
                time+=math.ceil(dist[i]/m)
            time+=dist[-1]/m

            

            if time <=hour:
                res=m
                r=m-1
            else:
               
                l=m+1

        return res

