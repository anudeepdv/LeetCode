class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res=[]
        for i in range(len(nums)):

            initial = nums[i]
            
            l= i+1
            
            r=len(nums)-1

            if i>=1 and nums[i]==nums[i-1]:
                continue

            while l<r:
                # print([initial,nums[i],nums[r]])
                val = initial+nums[l]+nums[r]

                if val>0:
                    r=r-1
                elif val<0:
                    l=l+1
                else:
                    
                    res.append([initial,nums[l],nums[r]])
                    while l+1<r-1 and nums[l]==nums[l+1] and nums[r]==nums[r-1]:
                        l=l+1
                        r=r-1
                    
                    l=l+1
                    r=r-1

                    

        return res
            