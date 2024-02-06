class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        ns =set(nums)
        res=1
        if len(nums)==0:
            return 0
        for i in ns:

            if i-1 not in ns:

                k=i
                temp=1
                while k+1 in ns:
                    temp+=1
                    res=max(res,temp)
                    k=k+1
        return res

        
