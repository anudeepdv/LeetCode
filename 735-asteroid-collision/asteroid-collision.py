class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s=deque()
        
        for a in asteroids:

            while s and s[-1]>0 and a<0:
                if abs(a)>abs(s[-1]):
                    s.pop()
                elif abs(a)==abs(s[-1]):
                    s.pop()
                    a=None
                    break
                else:
                    a=None
                    break

            if a:
                s.append(a)


        return list(s)
