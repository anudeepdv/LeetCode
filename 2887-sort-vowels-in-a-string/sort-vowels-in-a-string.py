class Solution:
    def sortVowels(self, s: str) -> str:
        
        l= [97,101,105,111,117,65,69,73,79,85]
        val=[]
        ind=[]
        s=list(s)
        for i in range(len(s)):
            if ord(s[i]) in l:
                val.append(s[i])
                ind.append(i)

        val.sort()
        k=0
        for i in ind:
            s[i]= val[k]
            k=k+1

        return ''.join(s)

        
            