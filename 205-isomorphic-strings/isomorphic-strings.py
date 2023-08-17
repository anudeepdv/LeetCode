class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        m={}
        for i in range(len(s)):
            
            if s[i] in m:
                if m[s[i]]!=t[i]:
                    return False
            else:
                if t[i] in m.values():
                    return False
                m[s[i]]=t[i]
        print(m)
        return True
        