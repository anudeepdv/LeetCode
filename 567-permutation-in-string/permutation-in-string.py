class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        a1 = sorted(s1)

        for i in range(0,len(s2)-len(s1)+1):
            if a1==sorted(s2[i:i+len(a1)]):
                return True

        return False