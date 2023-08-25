class Solution:
    def smallestSubsequence(self, s: str) -> str:

        d = collections.Counter(s)
        vis=set()

        q=[]

        for i in s:

            d[i]-=1

            if i not in vis:

                while q and q[-1]>i and d[q[-1]]:
                    vis.remove(q[-1])
                    q.pop()

                q.append(i)
                vis.add(i)

        return "".join(q)

