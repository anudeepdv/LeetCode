class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1]*n

    def find(self,node):
        cur = node
        while cur!=self.parent[cur]:
            cur=self.parent[cur]
        return cur

    def union(self,node1,node2):
        p1,p2 = self.find(node1),self.find(node2)

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

        for i in range(len(accounts)):
            for email in accounts[i][1:]:
                if email in email_to_id:
                    UF.union(i, email_to_id[email])
                else:
                    email_to_id[email]=i

        egroup = collections.defaultdict(list)

        for email , index in email_to_id.items():
            i = UF.find(index)
            egroup[i].append(email)

        print(egroup)

        res=[]

        for i in egroup:
            res.append([accounts[i][0]] + sorted(egroup[i]))

        return res
        