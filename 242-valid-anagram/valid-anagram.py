class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        count=collections.defaultdict(int)

        for i in s:
            count[i]+=1
        
        for i in t:
            if i not in count:
                return False
            else:
                count[i]-=1
                if count[i]==0:
                    del count[i]

        if len(count)==0:
            return True

        return False
       