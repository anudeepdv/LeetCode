class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        l = 0 
        r=len(nums)-1
        res= nums[0]

        while l<=r:
            if nums[l]<=nums[r]:
                res= min(res,nums[l])
                return res

            m = (l+r)//2

            if nums[l]<=nums[m]:
                res=min(res,nums[l])
                l=m+1
            else:
                res = min(nums[m],res)
                r=m-1

        return res