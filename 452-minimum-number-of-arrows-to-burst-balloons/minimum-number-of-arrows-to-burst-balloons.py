class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        

        res = 1

        points.sort(key = lambda x : x[1])
        key = points[0][1]
        for i in range(1,len(points)):
            ns,ne = points[i][0],points[i][1]

            if key in range(ns,ne+1):
                continue

            else:
                key = ne
                res+=1

        return res