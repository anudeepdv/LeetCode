class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        l = []
        if a>0:
            l.append((-a,'a'))
        if b>0:
            l.append((-b,'b'))
        if c>0:
            l.append((-c,'c'))
            
        
        heapify(l)

        # print(l)

        res=""
        while(l):

            if len(res)>=2 and res[-1]==res[-2]==l[0][1] :
                temp = heappop(l)
                if len(l)==0:
                    return res
                top = heappop(l)
                res=res+top[1]
                # top[0]=top[0]+1
                newtop= (top[0]+1,top[1])
                if newtop[0]!=0:
                    heappush(l, newtop)
                print(res)
                
                heappush(l, temp)
                print(l)
            else:
                top = heappop(l)
                res=res+top[1]
                print(res)
                newtop= (top[0]+1,top[1])
                if newtop[0]!=0:
                    heappush(l, newtop)
                print(l)

        return res