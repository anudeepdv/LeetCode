class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        pairs=[]

        for i in range(1,len(weights)):
            pairs.append(weights[i]+weights[i-1])

        pairs.sort()
        l=0
        r=0
        for i in range(k-1):
            l=l+pairs[i]
            r=r+pairs[len(pairs)-i-1]
        
        return r-l




