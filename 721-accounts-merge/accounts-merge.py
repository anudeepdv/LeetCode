class UnionFind:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find(self,node):
        cur = node
        while cur!=self.parent[cur]:
            cur=self.parent[cur]
        return cur

    def union(self,n1,n2):
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 == p2:
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
        
        UF = UnionFind(len(accounts))
        email_to_id = {}

        for i,l in enumerate(accounts):
            for email in l[1:]:
                if email in email_to_id:
                    UF.union(i, email_to_id[email])
                else:
                    email_to_id[email]=i

        id_to_emails = collections.defaultdict(list)

        for email in email_to_id:
            id = UF.find(email_to_id[email])
            id_to_emails[id].append(email)
        print(id_to_emails)
        res =[]

        for id in id_to_emails:
            res.append([accounts[id][0]]+sorted(id_to_emails[id]))

        return res

