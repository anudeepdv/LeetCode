class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        root=None
        adj=collections.defaultdict(list)
        for i,nums in enumerate(manager):
            if nums==-1:
                root=i
                continue
            adj[nums].append(i)

        if len(adj)==0:
            return 0

        q=collections.deque([])
        q.append([root,0])

        maxT=0
        while(q):
            for i in range(len(q)):

                parent,time = q.popleft()

                for nei in adj[parent]:
                    childTime = time+informTime[parent]
                    q.append([nei,childTime])
                    maxT=max(maxT,childTime)

        return maxT


        
        return 0
