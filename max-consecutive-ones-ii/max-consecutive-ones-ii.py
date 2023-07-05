class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        l=0
        res=0
        hashmap=collections.defaultdict(int)

        for r in range(len(nums)):
            hashmap[nums[r]]+=1
            while hashmap[0]==2:
                hashmap[nums[l]]-=1
                l=l+1

            res=max(res,r-l+1)
        return res