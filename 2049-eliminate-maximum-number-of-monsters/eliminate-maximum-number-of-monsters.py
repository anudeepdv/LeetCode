class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        res=[]
        for i in range(len(dist)):
           res.append(dist[i]/speed[i])

        res.sort()
        print(res)
       
        for i in range(len(res)):
            if res[i]<=i:
                return i
        return len(res)

