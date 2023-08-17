class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        l=s.split(" ")
        m={}
        if len(l)!=len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in m:
                if m[pattern[i]]!=l[i]:
                    return False
            else:
                if l[i] in m.values():
                    return False
                m[pattern[i]]=l[i]

        return True
            