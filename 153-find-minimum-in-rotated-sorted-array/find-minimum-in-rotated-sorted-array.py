class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        l = 0 
        r=len(nums)-1
        res= nums[0]

        while l<=r:

            m = (l+r)//2
            #Left is sorted
            if nums[l]<=nums[m]:
                res = min(res,nums[l])
                l=m+1
            else:
                res = min(res,nums[m])
                r=m-1

        return res

