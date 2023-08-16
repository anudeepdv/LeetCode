class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort()
        res=0
        n=len(citations)
        for i,v in enumerate(citations):

            if n-i<=citations[i]:
                res=n-i
                break

        return res