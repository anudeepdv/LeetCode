class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:

        adjlist = collections.defaultdict(list)

        for i in range(len(pid)):
            adjlist[ppid[i]].append(pid[i])

        print(adjlist)

        q=collections.deque()
        q.append(kill)
        res=[]
        while q:

            for _ in range(len(q)):
                pop = q.popleft()
                res.append(pop)

                for node in adjlist[pop]:
                    q.append(node)
        return res
