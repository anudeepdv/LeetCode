class Solution:
    def reorganizeString(self, s: str) -> str:

        c= collections.Counter(s)

        h=[(-cnt,ch) for ch,cnt in c.items()]

        heapq.heapify(h)

        prev=None
        res=""
        while h or prev:
            if prev and not h:
                return ""
            print(h)
            i,j = heapq.heappop(h)
            res=res+j
            i=i+1
            if prev:
                heapq.heappush(h,prev)
                prev=None
            if i!=0:
                prev=(i,j)

        return res




