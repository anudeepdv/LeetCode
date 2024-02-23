class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        ticketTable = [ float('inf') for i in range(n)]
        ticketTable[src]=0
        for i in range(k+1):

            temp = ticketTable.copy()

            for s,d,v in flights:
                if ticketTable[s]==float('inf'):
                    continue
                if v+ticketTable[s]<temp[d]:
                    temp[d]=v+ticketTable[s]
            
            ticketTable=temp

        return int(ticketTable[dst]) if ticketTable[dst] !=float('inf') else -1