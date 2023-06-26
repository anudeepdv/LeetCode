class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        lHeap =[]
        rHeap=[]

        for i in range(candidates):
            if costs:
                lHeap.append(costs[0])
                del costs[0]

        for i in range(candidates):
            if costs:
                rHeap.append(costs[-1])
                del costs[-1]

        
        heapq.heapify(lHeap)
        heapq.heapify(rHeap)

        s=0
        for i in range(k):

            if len(lHeap)==0 or len(rHeap)==0:

                if len(lHeap)==0:
                    s+=heapq.heappop(rHeap)
                    if costs:
                        heapq.heappush(rHeap,costs[-1])
                        del costs[-1]
                else:
                    s+=heapq.heappop(lHeap)
                    if costs:
                        # lHeap.append(costs[0])
                        heapq.heappush(lHeap,costs[0])
                        del costs[0]



            else:

                if lHeap[0]>rHeap[0]:
                    s+=heapq.heappop(rHeap)
                    if costs:
                        heapq.heappush(rHeap,costs[-1])
                        del costs[-1]
                else:
                    s+=heapq.heappop(lHeap)
                    if costs:
                        heapq.heappush(lHeap,costs[0])
                        del costs[0]

        return s


