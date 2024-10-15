class Solution:
    def maximumSwap(self, num: int) -> int:
        
        q = collections.deque()

        while num:

            a = num%10
            q.appendleft(a)
            num=num//10

        arr = collections.deque()

        max_seen, max_seen_i=-1,-1

        i=len(q)-1
        while i>=0:
            val = q[i]

            if val > max_seen:
                max_seen = val
                max_seen_i = i

            arr.appendleft([val,max_seen,max_seen_i])
            i-=1

        i = 0

        while i<len(arr):
            c,m,mi = arr[i]
            if m>c:
                print("J")
                arr[i][0],arr[mi][0]=arr[mi][0],arr[i][0]
                break
            i+=1

        res= 0
        for i in arr:
            res=res*10
            res+=i[0]
        
        return res