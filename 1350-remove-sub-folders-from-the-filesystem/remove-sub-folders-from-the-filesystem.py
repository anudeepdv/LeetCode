class TrieNode:
    def __init__(self):
        self.children={}
        self.eof=False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.res=[]
        
    def insert(self, fld: str) -> None:

        folder = fld.split('/')
        cur = self.root
        flag=True
        for w in folder:
           
            if w!="":
                if cur.eof:
                    flag=False
                if w not in cur.children:
                    cur.children[w]=TrieNode()

                cur=cur.children[w]
        cur.eof=True
        if flag:
            self.res.append(fld)

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        T = Trie()

        for f in folder:
            T.insert(f)

        return T.res

        
            

