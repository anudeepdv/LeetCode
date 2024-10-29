class Solution:
    def maximumSwap(self, num: int) -> int:
        
        q = deque()

        while num:
            q.appendleft(num%10)
            num=num//10

        maxseen = -1
        maxseeni = -1



        for i in range(len(q)-1,-1,-1):
            if q[i]>maxseen:
                maxseen = q[i]
                maxseeni =i 

            q[i]=(q[i],maxseen,maxseeni)

        print(q)

        for i in range(len(q)):
            if q[i][1]>q[i][0]:
                q[i],q[q[i][2]]=q[q[i][2]],q[i]
                break
        cur=0
        print(q)
        for i in range(len(q)):
            cur=cur*10 + q[i][0]

        return cur

