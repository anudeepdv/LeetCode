class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        
        intervals.sort(key = lambda x : x[0])

        s,e = intervals[0]
        res=[]
        for ns,ne in intervals[1:]:
            if e in range(ns,ne+1) or ns in range(s,e+1):
                e=max(e,ne)
                s=min(s,ns)
            else:
                print("t",s,e)
                res.append([s,e])
                s,e=ns,ne
                print("t",s,e)
        print("jj",s,e)
        res.append([s,e])

        return res
