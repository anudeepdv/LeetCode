class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        hashmap = collections.defaultdict(int)

        hashmap[0]=1

        pre=0
        tot=0
        for  i  in nums:
            pre=pre+i
            if pre - k in hashmap:
                tot = tot+ hashmap[pre - k ]

            hashmap[pre]+=1

        return tot
        