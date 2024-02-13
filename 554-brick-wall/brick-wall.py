class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:

        d= collections.defaultdict(int)
        d[0]=0
        for b in wall:
            c=0
            for i in b[:-1]:
                c=c+i
                d[c]+=1
        print(d)
        return len(wall)-max(d.values())


        