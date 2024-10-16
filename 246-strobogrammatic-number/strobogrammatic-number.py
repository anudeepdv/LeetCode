class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        d= {'0':'0','1':'1','6':'9','8':'8','9':'6'}

        l =0 
        r=len(num)-1

        while l<=r:
            if num[l] not in d:
                return False

            if d[num[l]]!=num[r]:
                return False

            l=l+1
            r=r-1

        return True