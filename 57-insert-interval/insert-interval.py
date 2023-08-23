class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        intervals.append(newInterval)
        intervals.sort(key=lambda x : x[0])
        res=[]
        s=[intervals[0][0],intervals[0][1]]
        added=None
        for i in intervals[1:]:
            
            if s[0]<=i[0]<=s[1]:
                s[1]=max(s[1],i[1])
                added=False
            else:
                added=True
                res.append(s)
                s=[i[0],i[1]]
        
        if s not in res:
            res.append(s)
        return res