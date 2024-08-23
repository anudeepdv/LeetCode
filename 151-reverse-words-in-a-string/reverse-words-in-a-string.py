class Solution:
    def reverseWords(self, s: str) -> str:
        
        l = 0
        r= 1
        while l< len(s) and s[l]==" ":
            l=l+1
        r=l+1
        res= []
        while r<len(s):
            # print(s[l:r])

            if s[r]==" ":
                if s[l:r]!="" and s[l:r]!=" " :
                    res.append(s[l:r])
                while  r<len(s) and s[r]==" ":
                    l=r+1
                    r=r+1
            r=r+1
        print(res)
        if s[l:r]!="" and s[l:r]!=" " :
            res.append(s[l:r])
        
        l= res[::-1]

        
        return " ".join(l)
