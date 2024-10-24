class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        rl = 0 
        res=""

        for i in range(len(s)):

            l,r=i,i
           
            while l>=0 and r <len(s) and s[l]==s[r]:
                if r-l+1 >rl:
                    rl=r-l+1
                    res = s[l:r+1]
                l=l-1
                r=r+1

            l,r=i-1,i

            while l>=0 and r <len(s) and s[l]==s[r]:
                if r-l+1 >rl:
                    rl=r-l+1
                    res = s[l:r+1]
                l=l-1
                r=r+1

        return res