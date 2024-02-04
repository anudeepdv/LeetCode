class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        s={}

        for i,val in enumerate(nums):
            if target - val in s:
                print(i,s[target - val])
                return [i,s[target - val]]
            s[val]=i

        