class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m= len(matrix)
        n= len(matrix[0])

        res=[]
        t=0
        b=m
        l=0
        r=n

        while len(res)<m*n:
            print(res)
            for i in range(l,r):
                res.append(matrix[t][i])
            t+=1

            for i in range(t,b):
                res.append(matrix[i][r-1])
            r=r-1

            print(l,r,t,b)
            if  not (l<r and t<b):
                break
            for i in range(r-1,l-1,-1):
                print(b,i)
                res.append(matrix[b-1][i])
            b-=1

            for i in range(b-1,t-1,-1):
                res.append(matrix[i][l])
            l+=1

        return res
        