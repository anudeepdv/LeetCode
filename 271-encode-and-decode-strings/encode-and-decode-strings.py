class Codec:
    
    def encode(self, strs: List[str]) -> str:
        res=''
        for i in strs:
            
            res= res+i+'π'
        res=res[:len(res)-1]
        return res
        """Encodes a list of strings to a single string.
        """
        

    def decode(self, s: str) -> List[str]:
        i=0
        l=[]
        
        
        
        return s.split('π')

        """Decodes a single string to a list of strings.
        """
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))