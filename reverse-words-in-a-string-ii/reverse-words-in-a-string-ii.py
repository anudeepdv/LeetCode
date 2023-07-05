class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

        l=0
        
        for r in range(len(s)):

            if s[r]==' ':
                print(l,r)
                print(s[l:r],s[r-1:l-1:-1])
                s[l:r]=reversed(s[l:r])
                l=r+1

        if(l!=len(s)-1):
             s[l:]=reversed(s[l:])

            