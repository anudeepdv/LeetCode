class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        minh =[(c,p) for c,p in zip(capital,profits)]
        maxh =[]

        heapify(minh)
        res = 0
        while k:

            while minh and minh[0][0]<=w:
                c,p = heappop(minh)
                heappush(maxh, -p)
            # print(maxh)
            if not maxh:
                return w
            w+= -1*heappop(maxh)
            
            k-=1

        return w