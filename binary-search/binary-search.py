class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary(l,r):
            
            if l>r:
                return -1
            m = l+(r-l)//2
            
            if nums[m]==target:
                return m

            elif target<nums[m]:
                return binary(l,m-1)
            elif target>nums[m]:
                return binary(m+1,r)

            else:
                return -1

           


        l,r=0,len(nums)-1

        return binary(l,r)


        


