class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        l = 0
        d = collections.defaultdict(int)
        res=0
        for r in range(len(nums)):
            d[nums[r]]+=1

            while d[0]>k:
                d[nums[l]]-=1
                l+=1

            res=max(res,r-l+1)

        return res

