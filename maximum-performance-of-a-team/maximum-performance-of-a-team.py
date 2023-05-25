class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:

        l = [(n1,n2) for n1,n2 in zip(speed,efficiency)]

        l=sorted(l,key= lambda x:x[1],reverse=True)
        print(l)
        h= []
       
        res=0
        nums=0
        for n1,n2 in l:
          

            heapq.heappush(h,n1)
            nums= nums+n1

            if(len(h)>k):
                popq = heapq.heappop(h)
                nums=nums-popq

            
            res = max(res,nums*n2)

        return res%1000000007


