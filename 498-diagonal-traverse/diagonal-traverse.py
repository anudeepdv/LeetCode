class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        rows= len(mat)
        cols=len(mat[0])
        res= []
        up=True
        r=c=0
        while len(res)< rows*cols:

            if up:

                while r>=0 and c<cols:
                    res.append(mat[r][c])
                    r-=1
                    c+=1
                
                if c==cols:
                    r+=2
                    c-=1
                else:
                    r+=1

                up=False

            else:

                while r<rows and c>=0:
                    res.append(mat[r][c])
                    r+=1
                    c-=1
                if r==rows:
                    r-=1
                    c+=2

                else:
                    c+=1

                up=True

        return res

