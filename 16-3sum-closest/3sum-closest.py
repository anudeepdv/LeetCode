class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        res=math.inf
        

        for  i in range(len(nums)):

            l = i+1
            r=len(nums)-1

            if i>0 and nums[i-1]==nums[i]:
                continue

            while l<r:
                # print(i,l,r)
                tot = nums[i]+nums[l]+nums[r]

                if tot == target:
                    return target
                
                if abs(tot-target) < abs(res-target):
                    res=tot
                if tot>target:
                    r-=1
                else:
                    l+=1

        return res