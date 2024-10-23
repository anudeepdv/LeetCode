class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        start = []
        end = []
        for s,e in intervals:

            start.append(s)
            end.append(e)

        start.sort()
        end.sort()

        i = 0 
        j = 0 
        res=0
        best = 0
        while i<len(start):
            if start[i]<end[j]:
                res+=1
                i+=1
            else:
                res-=1
                j+=1
            best = max(res,best)
        return best

