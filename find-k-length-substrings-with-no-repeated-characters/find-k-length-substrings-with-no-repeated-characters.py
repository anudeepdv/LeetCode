class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:

        l=0
        m=collections.defaultdict(int)
        c=0
        for r in range(len(s)):
            m[s[r]]+=1
            
            while max(m.values())==2:
                m[s[l]]-=1
                l=l+1
            while r-l+1>k:
                m[s[l]]-=1
                l=l+1

            if r-l+1==k:
                c+=1

        return c
