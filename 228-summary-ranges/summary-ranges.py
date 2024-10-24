class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        l=nums[0]
        prev=l
        res=[]
        for r in range(1,len(nums)):
            #break
            if prev+1!=nums[r]:
                # print(l,prev)
                if l==prev:
                    res.append(str(l))
                else:
                    res.append(str(l)+"->"+str(prev))
                l=nums[r]
                prev= l
            else:
                prev=nums[r]

        # print(l,prev)
        if l==prev:
            res.append(str(l))
        else:
            res.append(str(l)+"->"+str(prev))

        return res

            