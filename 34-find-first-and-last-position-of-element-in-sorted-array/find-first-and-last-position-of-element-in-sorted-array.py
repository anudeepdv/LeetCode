class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        

        def binary(l,r,left):
            res=-1
            while l<=r:
                m = (l+r)//2

                if target>nums[m]:
                    l=m+1
                elif target<nums[m]:
                    r=m-1
                else:
                    res=m
                    if left:
                        r=m-1
                    else:
                        l=m+1

            return res
        

        return [binary(0, len(nums)-1, True),binary(0, len(nums)-1, False)]