class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        j=0
        n=len(s)
        
        for i in t:
            if j==n:
                return True
            if i ==s[j]:
                j=j+1

        if j==n:
            return True

        return False