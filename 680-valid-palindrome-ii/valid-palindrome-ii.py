class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        l=0
        r=len(s)-1

        def tr(left,right):
            while left<=right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        while l<=r:

            if s[l]!=s[r]:
                return tr(l+1,r) or tr(l,r-1)

            l=l+1
            r=r-1

        return True

