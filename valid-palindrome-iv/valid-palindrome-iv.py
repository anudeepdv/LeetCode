class Solution:
    def makePalindrome(self, s: str) -> bool:

        n=len(s)
        c=0
        for i in range(n//2):
            if s[i]!=s[n-1-i]:
                c=c+1
        return c<=2