class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        res = [[p,s] for p,s in zip(position,speed)]
        print(res)
        s=collections.deque()
        res.sort(key=lambda x:x[0])
        res.reverse()
        for pos,t in res:
            s.append((target-pos)/t)
            if len(s)>=2 and s[-1]<=s[-2]:
                s.pop()
        return len(s)