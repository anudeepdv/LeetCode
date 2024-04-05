class SeatManager:

    def __init__(self, n: int):
        self.unres = [i for i in range(1,n+1)]
        heapq.heapify(self.unres)
        self.res=set()
        

    def reserve(self) -> int:

        a= heapq.heappop(self.unres)
        self.res.add(a)
        return a

        

    def unreserve(self, seatNumber: int) -> None:
        if seatNumber in self.res:
            self.res.remove(seatNumber)
            heapq.heappush(self.unres,seatNumber)
        

        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)