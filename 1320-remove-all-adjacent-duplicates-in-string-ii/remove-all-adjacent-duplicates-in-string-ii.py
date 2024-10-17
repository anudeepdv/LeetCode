class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        q=collections.deque()

        for i in s:
            
            if q and q[-1][0]==i:
                q[-1][1]+=1
                if q[-1][1]==k:
                    q.pop()
            else:
                q.append([i,1])

        res=""

        for v,i in q:
            res+=v*i
        return res