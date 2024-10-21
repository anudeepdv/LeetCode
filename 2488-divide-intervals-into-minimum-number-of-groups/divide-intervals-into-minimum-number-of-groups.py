class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        
        start = []
        end = []

        for s,e in intervals:
            start.append(s)
            end.append(e)

        start.sort()
        end.sort()

        group = 0

        i=0
        j=0
        res=0

        while i <len(start):

            if start[i]<=end[j]:
                group+=1
                i+=1
            else:
                group-=1
                j+=1

            res=max(res,group)

        return res

