class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        hashMap = collections.defaultdict(int)

        l=0
        r=0
        res=0
        for r in range(len(nums)):
            hashMap[nums[r]]+=1
            print(hashMap)
            while hashMap[0]==2:
                hashMap[nums[l]]-=1
                l=l+1
                
            print(l,r)
            
            res=max(res,r-l+1-1)

        return res

            

