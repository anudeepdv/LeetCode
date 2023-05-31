class UndergroundSystem:

    def __init__(self):
        self.checkInTimeMap=collections.defaultdict(int)
        self.checkInStationMap=collections.defaultdict(str)
        self.averageMap = collections.defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInTimeMap[id]=t
        self.checkInStationMap[id]=stationName
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:

        timeTaken = t-self.checkInTimeMap[id]
        self.averageMap[self.checkInStationMap[id]+'_'+stationName].append(timeTaken)
        del self.checkInTimeMap[id]
        del self.checkInStationMap[id]

        

    def getAverageTime(self, startStation: str, endStation: str) -> float:

        time = sum(self.averageMap[startStation+'_'+endStation])

        return time/len(self.averageMap[startStation+'_'+endStation])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)