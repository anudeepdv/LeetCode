class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)
        res=0
        for i in range(n):

            l= i 
            r=i

            while l>=0 and r<n and s[r]==s[l]:
                res=res+1

                l=l-1
                r=r+1

            l= i 
            r=i+1

            while l>=0 and r<n and s[r]==s[l]:
                res=res+1

                l=l-1
                r=r+1

        return res
            
            