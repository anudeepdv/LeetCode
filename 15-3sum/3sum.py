class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        res=set()
        for i in range(len(nums)-1):
            l = i+1
            r= len(nums)-1

            while l<r:
                v= nums[i]+nums[l]+nums[r]

                if v==0:
                    res.add((nums[i],nums[l],nums[r]))
                    l+=1
                elif v>0:
                    r-=1
                else:
                    l+=1

        return list(res)
