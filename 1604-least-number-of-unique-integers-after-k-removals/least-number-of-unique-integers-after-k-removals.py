class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        h=[]
        heapq.heapify(h)

        d=collections.Counter(arr)

        for k1,v in d.items():
            # print(v,k)
            heapq.heappush(h,[v,k1])

        for i in range(k):
            if(h):
                c,v = heapq.heappop(h)
                print(c,v)
                if c-1 !=0:
                    heapq.heappush(h,[c-1,v])

        return len(h)


