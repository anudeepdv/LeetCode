class Solution:
    def validPalindrome(self, s: str) -> bool:
        #TIme - O(n) Space O(1)
        def valid(l,r):

            while l<=r:
                if s[l]!=s[r]:
                    return False
                l=l+1
                r=r-1

            return True

        l = 0
        r=len(s)-1

        while l<=r:
            if s[l]!=s[r]:
                return valid(l+1,r) or valid(l,r-1)
            
            l+=1
            r-=1

        return True