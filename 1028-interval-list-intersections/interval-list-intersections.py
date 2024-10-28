class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        
        i = 0
        j=0
        res=[]

        while i<len(firstList) and j<len(secondList):
            sa,ea = firstList[i]
            sb,eb = secondList[j]

            if sa in range(sb,eb+1):
                sn = sa
                en=None

                if ea<eb:
                    en = ea
                    i+=1
                else:
                    en =eb
                    j+=1
                res.append([sn,en])
            elif sb in range(sa,ea+1):
                sn =sb
                en= None

                if ea<eb:
                    en = ea
                    i+=1
                else:
                    en =eb
                    j+=1
                res.append([sn,en])

            elif ea<eb:
                i+=1
            else:
                j+=1

        return res
