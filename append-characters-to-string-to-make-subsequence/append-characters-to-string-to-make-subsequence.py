class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i =0 
        j=0

        while i< len(s):
            if j in range(len(t)) and s[i]==t[j]:
                i=i+1
                j=j+1
            else:
                i=i+1

        return len(t)-j