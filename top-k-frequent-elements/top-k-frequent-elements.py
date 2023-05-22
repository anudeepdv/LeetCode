class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        countD = {}

        for i in nums:
            countD[i]=countD.get(i,0)+1

        d =[[] for i in range(len(nums)+1)]
        for l , v in countD.items():
            d[v].append(l)

        res= []
        print(d)
        for i in range(len(d)-1,-1,-1):
            print(i)
            for j in d[i]:
                res.append(j)
                print(len(res),k)
                if len(res)==k:
                    return res

            


