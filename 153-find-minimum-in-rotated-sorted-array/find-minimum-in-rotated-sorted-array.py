class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r=len(nums)-1

        res= nums[l]

        while l<=r:

            if nums[l]<=nums[r]:
                res=min(res,nums[l])
                break

            m = (l+r)//2
            print(m)
            if nums[r]<nums[m]:
                res=min(res,nums[m])
                l=m+1
            else:
                res=min(res,nums[m])
                r=m-1

        return res

            
        