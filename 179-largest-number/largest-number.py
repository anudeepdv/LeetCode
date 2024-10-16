class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        for i in range(len(nums)):
            nums[i]=str(nums[i])

        def cmp(n1,n2):
            if n1+n2>n2+n1:
                return -1
            return 1

        nums.sort(key = cmp_to_key(cmp))

        return str(int("".join(nums)))