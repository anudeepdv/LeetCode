class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        cur  = 0
        res=[]
        r=0
        c=0

        up =True

        rows = len(mat)
        cols = len(mat[0])
        while len(res) < len(mat)*len(mat[0]):
            # print(res)
            if up:

                while r>=0 and c<cols:
                    res.append(mat[r][c])
                    cur+=1
                    r=r-1
                    c=c+1

                if c==cols:
                    r+=2
                    c-=1
                else:
                    r+=1
                
                up=False
            else:

                while r<rows and c>=0:
                    res.append(mat[r][c])
                    cur+=1
                    r+=1
                    c-=1

                if r==rows:
                    r-=1
                    c+=2
                else:
                    c=c+1
                up=True
            
            

        return res
