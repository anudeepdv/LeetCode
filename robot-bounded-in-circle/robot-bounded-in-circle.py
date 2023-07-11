class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        dirx, diry= (0,1)
        x,y=0,0
        for i in instructions:

            if i =='G':
                x,y=x+dirx,y+diry
            elif i== 'L':
                dirx, diry = -diry,dirx
            else:
                dirx,diry= diry,-dirx

        if (x,y)==(0,0) or (dirx,diry)!=(0,1):
            return True
        return False


