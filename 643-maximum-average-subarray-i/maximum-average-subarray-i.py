class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        s = sum(nums[:k])
        m=s
        for i in range(k,len(nums)):
            print(s,nums[i-k],nums[i])
            s=s-nums[i-k]+nums[i]
            print(s)
            m=max(m,s)

        return m/k


