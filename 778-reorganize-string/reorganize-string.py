class Solution:
    def reorganizeString(self, s: str) -> str:
        
        c = Counter(s)
        
        h = [(-val,ch) for ch,val in c.items()]
        heapify(h)
        print(h)
        prev=None
        res=''
        while h or prev :
            if not h:
                return ""
            count,ch = heappop(h)
            res+=ch

            if prev:
                print(prev)
                heappush(h, prev)
            count+=1
            if count!=0:
                prev=(count,ch)
            else:
                prev=None

        return res

