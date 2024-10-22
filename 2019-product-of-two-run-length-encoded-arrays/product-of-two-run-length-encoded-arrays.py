class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        
        res= []
        i=0
        j=0

        prev=None
        while i <len(encoded1) and j<len(encoded2):
            val = None
            if encoded1[i][1]==encoded2[j][1]:
                val=[encoded1[i][0]*encoded2[j][0],encoded1[i][1]]
                i+=1
                j+=1
            elif encoded1[i][1] >encoded2[j][1]:
                val=[encoded1[i][0]*encoded2[j][0],encoded2[j][1]]
                encoded1[i][1]-=encoded2[j][1]
                j+=1
            else:
                val=[encoded1[i][0]*encoded2[j][0],encoded1[i][1]]
                encoded2[j][1]-=encoded1[i][1]
                i+=1

            if prev:
                if val[0]==prev[0]:
                    prev = [prev[0],prev[1]+val[1]]
                else:
                    res.append(prev)
                    prev=val
            else:
                prev=val

        if prev:
            res.append(prev)
        return res



