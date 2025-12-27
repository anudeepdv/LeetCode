class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        s=""
        for i in strs:
            s=s+str(len(i))+'#'+i
        return s
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        res =[]

        while i <len(s):
            j =i 
            while s[j]!='#':
                j+=1
            l = int(s[i:j])
            res.append(s[j+1:j+l+1])
            i=j+1+l
        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))