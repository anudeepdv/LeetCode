class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort()
        res=0
        for i,num in enumerate(citations):
            if citations[i]>=len(citations)-i:
                res=max(res,len(citations)-i)

        return res

