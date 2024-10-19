class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        
        c= {}
        for i,v in enumerate(order):
            c[v]=i

        for  i in range(len(words)-1):
            for j in range(len(words[i])):
                if j ==len(words[i+1]):
                    return False
                if words[i][j]!= words[i+1][j]:
                    if c[words[i][j]]>c[words[i+1][j]]:
                        return False
                    else:
                        break


        return True

