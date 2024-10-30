class Solution:
    def reorganizeString(self, s: str) -> str:
        
        c = Counter(s)
        
        h = [(-val,ch) for ch,val in c.items()]
        heapify(h)
        print(h)
        prev=None
        res=''
        
        while h or prev:
            if not h:
                return ""
            c,ch = heappop(h)
            if prev:
                heappush(h, prev)
                prev=None
            res+=ch
            c+=1
            if c!=0:
                prev=(c,ch)
        return res
