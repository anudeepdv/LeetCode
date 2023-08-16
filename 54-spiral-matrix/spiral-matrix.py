class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m= len(matrix)
        n= len(matrix[0])

        res=[]
        t=0
        b=m-1
        l=0
        r=n-1

        while len(res)<m*n:

            for i in range(l,r+1):
                res.append(matrix[t][i])

            for i in range(t+1,b+1):
                res.append(matrix[i][r])
            if t!=b:
                for i in range(r-1,l-1,-1):
                    res.append(matrix[b][i])
            if l!=r:
                for i in range(b-1,t,-1):
                    res.append(matrix[i][l])
            print(res)
            t=t+1
            b=b-1
            l=l+1
            r=r-1

        return res

