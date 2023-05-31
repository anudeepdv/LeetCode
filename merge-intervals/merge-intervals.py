class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        res=[]
       
        intervals=sorted(intervals, key =lambda x:x[0] )
        print(intervals)

        start=intervals[0][0]
        end=intervals[0][1]

        for i in range(1,len(intervals)):

            newx= intervals[i][0]

            if newx >= start and newx<=end:
                end = max(end,intervals[i][1])

            else:
                res.append([start,end])
                start=newx
                end = max(end,intervals[i][1])

        if [start,end] not in res:
            res.append([start,end])
        return res