class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        n = set(nums)
        res=0
        for i in n:

            if i-1 not in n:
                
                k=i
                t=1
                while k+1 in n:
                    print(k+1)
                    t=t+1
                    k=k+1
                print(i,k)
                res=max(res,k-i+1)

        return res