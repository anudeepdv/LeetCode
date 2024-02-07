class Solution:
    def frequencySort(self, s: str) -> str:
        
        d = collections.defaultdict(int)

        for i in s:
            d[i]+=1

        h=[(-i,j) for j ,i in d.items()]
        heapq.heapify(h)

        res=""

        while(h):
            a=heapq.heappop(h)
            res=res+(a[0]*-1*a[1])

        return res