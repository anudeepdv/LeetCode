class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        res = [i for i in zip(position,speed)]
       
        res.sort(reverse=True,key= lambda x:x[0])

        print(res)

        q= collections.deque()
        for i in res:

            time = (target-i[0])/i[1]

            q.append(time)

            while len(q)>=2 and q[-1]<=q[-2]:
                q.pop()

        return len(q)