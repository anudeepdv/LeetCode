class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        x0,y0= coordinates[0]
        x1,y1= coordinates[1]


        m = (y1-y0)/(x1-x0) if (x1-x0)!=0   else math.inf
        print(m)
        slope=True


        for xi,yi in coordinates[2:]:

            m1= (yi-y0)/(xi-x0) if xi-x0!=0   else math.inf
            print(m1)

            if m1!=m:
                return False

        return True
