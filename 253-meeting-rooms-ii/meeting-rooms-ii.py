class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        start = []
        end = [ ]

        for a,b in intervals:
            start.append(a)
            end.append(b)


        start.sort()
        end.sort()

        i = 0
        j=0
        res=0
        best = 0
        while i<len(start) and j<len(end):
            if start[i]<end[j]:
                i+=1
                res+=1
            else:
                j+=1
                res-=1
            best = max(best,res)

        return best

