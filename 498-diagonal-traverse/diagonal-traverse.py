class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        res = []

        up =True
        m=len(mat)
        n=len(mat[0])
        i=0
        j=0
        while len(res)<n*m:

            if up:
                
                while i in range(m) and j in range(n):
                    res.append(mat[i][j])
                    i-=1
                    j+=1
                
                if j==n:
                    i+=2
                    j-=1
                else:
                    i+=1
                
                up=False

            else:
                while i in range(m) and j in range(n):
                    res.append(mat[i][j])
                    i+=1
                    j-=1

                if i==m:
                    i-=1
                    j+=2
                else:
                    j+=1

                up=True


        return res

        


