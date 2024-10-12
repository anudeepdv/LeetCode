class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList.append(beginWord)

        adj = collections.defaultdict(list)
        for word  in wordList:
            for i in range(len(word)):
                pattern  = word[:i]+"*"+word[i+1:]
                adj[pattern].append(word)

        q = collections.deque([(beginWord,1)])

        vis = set()
        vis.add(beginWord)

        # print(adj)
        while q:
            # print("UOL")
            for _ in range(len(q)):
                
                word, r = q.popleft()
                # print("Porcessing Word", word)
                if word == endWord:
                    return r

                for i in range(len(word)):
                    pattern  = word[:i]+"*"+word[i+1:]
                    # print(word,pattern,"pat")
                    for  nei in adj[pattern]:
                        # print(nei,pattern,vis)
                        if nei not in vis:
                            # print("koo",nei)
                            q.append((nei,r+1))
                            # print("koo",nei,q)
                            vis.add(nei)

        return 0