class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        
        cs,ce = newInterval
        
        res=[]
        for i in range(len(intervals)):
            s,e = intervals[i]
            print(cs,ce,s,e)
            if cs is not None and  (cs in range(s,e+1) or s in range(cs,ce+1)):
                
                cs = min(cs,s)
                ce=max(ce,e)
                print(cs,ce)
            else:
                if cs is not None:
                    if ce<s:
                        res.append([cs,ce])
                        cs,ce=None,None
                res.append([s,e])

        if cs is not None:
            res.append([cs,ce])

        return res



                
