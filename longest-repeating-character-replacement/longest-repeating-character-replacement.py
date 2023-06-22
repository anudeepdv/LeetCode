class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l=0
        r=0
        n = len(s)

        hashMap =collections.defaultdict(int)
        res=0
        for r in range(n):

            hashMap[s[r]]+=1

            while r-l+1 - max(hashMap.values()) >k:
                 hashMap[s[l]]-=1
                 l=l+1
                
            res=max(res,r-l+1)

        return res