class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d=collections.defaultdict(int)

        for i in nums:
            d[i]+=1

        s=collections.defaultdict(list)
        for key,val in d.items():
            s[val].append(key)

        res=[]
        for i in range(len(nums),-1,-1):
          
            for j in s[i]:
                res.append(j)
                if len(res)==k:
                    return res