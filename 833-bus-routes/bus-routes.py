class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        m=collections.defaultdict(set)

        for i, n in enumerate(routes):
            for node in n:
                m[node].add(i)

        vis=set()
        q=collections.deque()
        q.append(source)
        res=-1
        while q:
            res+=1
            for _ in range(len(q)):
                cur = q.popleft()
                if cur==target:
                    return res

                for bus in m[cur]:
                    if bus not in vis:
                        vis.add(bus)
                        q.extend(routes[bus])


        return -1


        