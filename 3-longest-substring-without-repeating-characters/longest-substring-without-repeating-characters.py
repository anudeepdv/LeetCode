class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curset = set()
        l =0 
        r= 0
        res=0
        while r< len(s):
            while s[r] in curset:
                curset.remove(s[l])
                l+=1
            curset.add(s[r])
            r+=1
            res=max(res,r-l)
        return res


        