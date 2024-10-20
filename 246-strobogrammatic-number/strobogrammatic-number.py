class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        d= {'0':'0','1':'1','6':'9','8':'8','9':'6'}

        l =0 
        r=len(num)-1

        while l<=r:
            if num[l] in d and num[r]==d[num[l]]:
                l+=1
                r-=1
            else:
                return False

        return True