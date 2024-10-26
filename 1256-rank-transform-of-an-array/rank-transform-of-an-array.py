class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        if not arr:
            return []
        sort = sorted(arr)

        rank=1

        m= {sort[0]:1}

        for i in range(1,len(sort)):
            if sort[i-1]==sort[i]:
                continue
            else:
                rank+=1
                m[sort[i]]=rank

        res=[]

        for i in arr:
            res.append(m[i])

        return res

