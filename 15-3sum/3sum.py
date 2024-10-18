class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res=[]
        i=0
        while i<len(nums):

            if i>=1 and nums[i]==nums[i-1]:
                i+=1
                continue
            
            l = i +1 
            r = len(nums)-1

            while l<r:
                cursum = nums[i]+nums[l]+nums[r]
                if cursum>0:
                    r-=1
                elif cursum<0:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l-1]==nums[l]:
                        l+=1

            i=i+1


        return res

            
