class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        h= collections.defaultdict(int)

        for i in magazine:
            h[i]+=1

        
        for i in ransomNote:
            if i in h:
                h[i]-=1
                if h[i]==0:
                    del h[i]
            else:
                return False

        return True