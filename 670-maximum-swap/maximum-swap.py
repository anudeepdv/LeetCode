class Solution:
    def maximumSwap(self, num: int) -> int:
        
        q = deque()

        cur = num

        while cur!=0:
            q.appendleft(cur%10)
            cur=cur//10

        
        i = len(q)-1
        maxseen = -1 
        maxseeni=-1

        while i>=0:
            cur = q[i]
            if cur>maxseen:
                maxseen = cur
                maxseeni = i
            q[i]=(cur,maxseen,maxseeni)
            i-=1

        print(q)
        
        for i in range(len(q)):
            if q[i][1]>q[i][0]:
                q[i],q[q[i][2]]=q[q[i][2]],q[i]
                break

        


        res=0 
        for i in q:
            res=res*10+i[0]

        return res