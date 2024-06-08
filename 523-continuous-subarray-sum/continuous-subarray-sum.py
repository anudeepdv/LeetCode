class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        m={0:-1}
        s=0
        for i in range(len(nums)):
            s=s+nums[i]
            rem = s%k

            if rem in m:
                if i-m[rem]>1:
                    return True

            else:
                m[rem]=i

        return False
