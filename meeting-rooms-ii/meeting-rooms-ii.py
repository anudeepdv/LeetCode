class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        c=0

        res=0

        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        i=0
        j=0
        while i<len(start):
            if start[i]<end[j]:
                c=c+1
                i=i+1
            else:
                c=c-1
                j=j+1
            res=max(res,c)

        return res
