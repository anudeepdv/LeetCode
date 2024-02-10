class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        d=collections.defaultdict(int)

        for i in s:
            d[i]+=1
            if d[i]==2:
                del d[i]

        if len(d)==1 or len(d)==0:
            return True
        else:
            return False
