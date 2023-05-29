class treenode:
    
    def __init__(self):
        self.children = {}
        self.end=False


class WordDictionary:

    def __init__(self):
        self.root = treenode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for i in word:
            
            if i in curr.children:
                curr=curr.children[i]
            else:
                curr.children[i]=treenode()
              
                curr=curr.children[i]
                
        curr.end=True
        

    def search(self, word: str) -> bool:
        def dfs(j,curr):
           
            for i in range(j,len(word)):

                c = word[i]
                    
                if c=='.':
                    
                    for v in curr.children.values():
                        if word=='a.d':
                            print(v.children)
                        if dfs(i+1,v):
                            return True
                    return False
                else:

                    if c in curr.children:
                        curr=curr.children[c]
                    else:
                        return False
            return curr.end

        return dfs(0,self.root)


