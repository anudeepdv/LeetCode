class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        intervals = sorted(intervals,key=lambda x:x[0])

        if len(intervals)==0:
            return True

        end = intervals[0][1]

        for i in intervals[1:]:

            if end>i[0]:
                return False
            end = i[1]

        return True