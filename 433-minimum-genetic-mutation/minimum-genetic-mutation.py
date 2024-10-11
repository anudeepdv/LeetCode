class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        def getdiff(a,b):
            c=0
            for i in range(len(a)):
                if a[i]!=b[i]:
                    c+=1
            
            if c==1:
                return True
            
            return False

        adj = collections.defaultdict(list)

        for i in range(len(bank)):
            for j in range(i+1,len(bank)):

                a,b = bank[i],bank[j]

                if getdiff(a,b):
                    adj[a].append(b)
                    adj[b].append(a)

        for i in range(len(bank)):
            a= startGene
            b= bank[i]
            if getdiff(a,b):
                adj[a].append(b)
                adj[b].append(a)


        q=collections.deque([(startGene,0)])
        vis = set()

        print(adj)

        while q:

            cur,move = q.popleft()

            if cur ==endGene:
                return move

            vis.add(cur)

            for nei in adj[cur]:
                if nei not in vis:
                    q.append((nei,move+1))

        return -1