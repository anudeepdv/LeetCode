class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        c = Counter(nums)

        d = [[] for i in range(len(nums)+1)]
        print(c,d)
        for key,val in c.items():
            d[val].append(key)

        res= []
        for i in range(len(d)-1,-1,-1):
            for val in d[i]:
                res.append(val)
                k-=1
                if k==0:
                    return res
