class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        c = Counter(nums)

        d = [[] for i in range(len(nums)+1)]
        
        for key,count in c.items():
            d[count].append(key)

        res=[]
        for i in range(len(d)-1,-1,-1):

            for key in d[i]:
                res.append(key)
                k-=1
                if k ==0:
                    return res
