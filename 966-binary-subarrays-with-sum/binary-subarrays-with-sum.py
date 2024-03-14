class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def help(x):

            if x<0:
                return 0

            l=0
            r=0
            cur=0
            res=0
            for r in range(len(nums)):
                cur+=nums[r]
                while cur>x:
                    cur-=nums[l]
                    l=l+1

                res+=r-l+1

            return res

        return help(goal)-help(goal-1)