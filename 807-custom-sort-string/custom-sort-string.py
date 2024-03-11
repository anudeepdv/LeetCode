class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        c = Counter(s)
        res=""
        for i in order:
            if i in c:
                res=res+i*c[i]
                del c[i]

        for i in c:    
            res=res+i*c[i]
           
        print(res)
        return res