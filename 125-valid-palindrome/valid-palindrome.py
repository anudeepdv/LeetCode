class Solution:
    def isPalindrome(self, s: str) -> bool:
        

       
        res = ''
        for v in s:
            if ord(v) in range(97,123) or  ord(v) in range(65,91) or  ord(v) in range(48,58):
                res=res+v.lower()
        l,r=0,len(res)-1
        print(res)
        while l<=r:
            if res[l]!=res[r]:
                return False 
            l+=1
            r-=1
        return True      