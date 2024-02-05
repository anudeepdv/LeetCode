class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """

        res=""
        res+=','.join([str(len(i)) for i in strs])
        res+='*'
        res+=''.join(strs)
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        inital = s.split("*")[0]
        lens = inital.split(',')
        res=[]
        i=s.index("*")+1

        for val in lens:
            res.append(s[i:i+int(val)])
            i = i+int(val)

        return res
        
        
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))