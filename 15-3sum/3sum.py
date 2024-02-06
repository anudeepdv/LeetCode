class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res=[]
        for i in range(len(nums)):

            initial = nums[i]
            l= i+1
            if i>=1 and nums[i]==nums[i-1]:
                continue

            r=len(nums)-1

            while l<r:
                # print([initial,nums[i],nums[r]])
                val = initial+nums[l]+nums[r]

                if val>0:
                    r=r-1
                elif val<0:
                    l=l+1
                else:
                    res.append([initial,nums[l],nums[r]])
                    l=l+1
                    while(nums[l]==nums[l-1] and l<r  ):
                        l=l+1

        return res
            