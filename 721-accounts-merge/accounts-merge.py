class UnionFind:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank =[1]*n

    def find(self, n1):
        cur =n1
        while cur != self.parent[cur]:
            cur = self.parent[cur]
        return cur

    def union(self,n1,n2):
        p1  = self.find(n1)
        p2  = self.find(n2)

        if p1==p2:
            return False

        if self.rank[p1]>self.rank[p2]:
            self.rank[p1]+=self.rank[p2]
            self.parent[p2]=p1
        else:
            self.rank[p2]+=self.rank[p1]
            self.parent[p1]=p2

        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        uf = UnionFind(len(accounts))

        emailToId = {}

        for i,l in enumerate(accounts):
            for email in l[1:]:
                if email in emailToId:
                    uf.union(i, emailToId[email])
                else:
                    emailToId[email] = i

        egroup = collections.defaultdict(list)

        for email,i in emailToId.items():
            leader = uf.find(i)
            egroup[leader].append(email)

        print(egroup)

        res =[]

        for i , emails in egroup.items():
            res.append([accounts[i][0]] + sorted(emails))

        return res

        