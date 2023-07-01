class Solution:
    def alienOrder(self, words: List[str]) -> str:

        adjList ={c:set() for word in words for c in word}

        print(adjList)

        for i in range(len(words)-1):
            word1 =words[i]
            word2= words[i+1]

            minDist = min(len(word1),len(word2))
            if len(word1)> len(word2) and  word1[:minDist]==word2[:minDist]:
                return ""

            for j in range(minDist):
                if word1[j]!=word2[j]:
                    adjList[word1[j]].add(word2[j])
                    break
        print(adjList)
        
        vis={}
        path=[]
        def dfs(i):
            if i in vis:
                return vis[i]

            vis[i]=True

            for nei in adjList[i]:
                if dfs(nei):
                    return True
                
            vis[i]=False

            path.append(i)

        for i in adjList:
            if dfs(i):
                return ""

        return ''.join(path[::-1])
        
            



