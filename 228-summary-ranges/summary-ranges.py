class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        start=nums[0]
        end=nums[0]
        res=[]
        for i in nums[1:]:
            if i==end+1:
            
                end=i
                
            else:
                if end==start:
                    res.append(str(start))
                else:
                    res.append(str(start)+'->'+str(end))
                start=i
                end=i

        if start==end:
            if str(start) not in res:
                res.append(str(start))
        else:
            if str(start)+'->'+str(end) not in res:
                res.append(str(start)+'->'+str(end))
        return res


        