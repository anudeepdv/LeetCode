class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        
        i=0
        res=1


        for c  in target:

            i = source.find(c,i)

            if i==-1:

                i = source.find(c)
                res=res+1

                if i==-1:
                    return -1
            i=i+1

        return res
