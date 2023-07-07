class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        res=0
        while l<r:

            if nums[l]+nums[r]==k:
                res+=1

                # while l<r and nums[l]==nums[l+1]:
                #     l=l+1

                # while l<r and nums[r]==nums[r-1]:
                #     r=r-1

                l+=1
                r-=1

            elif nums[l]+nums[r]>k:
                r=r-1
            else:
                l=l+1

        return res 

