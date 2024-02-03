class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        c=collections.defaultdict(int)
        for i in s:
            c[i]+=1
        
        for i in t:
            c[i]-=1
            if c[i]==0:
                del c[i]

        if len(c)==0:
            return True
        return False
