class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        d={}
        res=0
        for i in nums :
            if i not in d:
                d[i]=1

            else:
                res=res+d[i]
                d[i]+=1

        return res
