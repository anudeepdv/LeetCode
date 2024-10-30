class TrieNodee:
    def __init__(self):
        self.children = {}
        self.eod = False

class Trie:
    def __init__(self):
        self.root=TrieNodee()

    def addword(self,word):
        cur = self.root

        for w in word:
            
            if w not in cur.children:
                cur.children[w] = TrieNodee()
            cur =cur.children[w]

        cur.eod=True
    
    def checkprefix(self):
        cur =self.root

        res=""
       
        while cur :
            print(cur.children.keys())
            if len(cur.children)==1:
                res+=list(cur.children.keys())[0]
                cur=cur.children[list(cur.children.keys())[0]]
            else:
                break
            if cur.eod==True:
                break
            
        
        return res
                

    

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        trie = Trie()

        for w in strs:
            if not w:
                return ""
            trie.addword(w)

        return trie.checkprefix()
