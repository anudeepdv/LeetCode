class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        start=None
        end=None
        res=[]
        for i in nums:

            if start is None and end is None:
                start=i
                end=i

            elif start is not None and end  is  not None:

                if i==end+1:
                    end=i
                else:
                    if start!=end:
                        res.append(str(start)+'->'+str(end))
                    else :
                        res.append(str(start))

                    start=i
                    end=i

        

                    
        if start is not None and end  is  not None:
            if start!=end:
                res.append(str(start)+'->'+str(end))
            else :
                res.append(str(start))

        return res

            