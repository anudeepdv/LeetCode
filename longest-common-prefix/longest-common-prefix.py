class TrieNode:
    def __init__(self) -> None:
        self.children={}
        self.end=False

class Trie:
    def __init__(self) -> None:
        self.root=TrieNode()

    def insert(self,word):

        cur=self.root

        for i in word:
            if i in cur.children:
                cur=cur.children[i]
            else:
                cur.children[i]=TrieNode()
                cur=cur.children[i]

        cur.end=True



    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs)==0:
            return ''

        trie= Trie()

        for i in strs:
            trie.insert(i)


        res=''
        
        cur=trie.root

        while cur and len(cur.children)==1 and cur.end==False:
            key=list(cur.children.keys())[0]
            res=res+key
            cur=cur.children[key]

        return res
