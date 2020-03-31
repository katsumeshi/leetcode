class UndergroundSystem(object):

    def __init__(self):
        self.start = {}
        self.savedTime = {}

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.start[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        startStation, startTime = self.start[id]
        prevTime, count = 0, 0
        if (startStation, stationName) in self.savedTime:
            prevTime, count = self.savedTime[(startStation, stationName)]
        self.savedTime[(startStation, stationName)] = (prevTime+t-startTime, count+1)
        

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        time, count = self.savedTime[(startStation, endStation)]
        return time/(count*1.0)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
