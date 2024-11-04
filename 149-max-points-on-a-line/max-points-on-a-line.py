class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        if (len(points)==1):
            return 1
        pointdict=dict()
        
        maxRange= 2
        for i in range(len(points)-1):
            slopeDict=dict()
            for j in range(len(points)):
                if(i!=j):
                    if(points[j][0]-points[i][0]==0):
                        slope = -10000000000
                    else:
                        print(i,j)
                        slope = (points[j][1]-points[i][1])/(points[j][0]-points[i][0])
                    
                    if slope in slopeDict:
                        slopeDict[slope]=slopeDict[slope]+1
                    else:
                        slopeDict[slope]=2

            print(slopeDict)
            if max(slopeDict.values()) > maxRange:
                maxRange= max(slopeDict.values())
        return maxRange
       




                

