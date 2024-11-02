class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        
        res= []
        i=0
        j=0

        while i<len(encoded1) and j<len(encoded2):
            val =None
            count=None
            if encoded1[i][1]==encoded2[j][1]:
                val = encoded1[i][0]*encoded2[j][0]
                count = encoded1[i][1]
                i+=1
                j+=1
            elif encoded1[i][1]<encoded2[j][1]:
                val = encoded1[i][0]*encoded2[j][0]
                count = encoded1[i][1]
                encoded2[j][1]-=count
                i+=1
            else:
                val = encoded1[i][0]*encoded2[j][0]
                count = encoded2[j][1]
                encoded1[i][1]-=count
                j+=1

            if res and res[-1][0]==val:
                res[-1][1]+=count
            else:
                res.append([val, count])

            # print(res)

        return res

            
                