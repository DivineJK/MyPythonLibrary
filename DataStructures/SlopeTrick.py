from heapq import heappush, heappop
class SlopeTrick:
    def __init__(self, initialValue = 0, aLeftInf = -int(1e13), aRightInf = int(1e13)):
        self.leftInf = aLeftInf
        self.rightInf = aRightInf
        self.l = []
        self.r = []
        self.lCount = 0
        self.rCount = 0
        self.minimum = initialValue
    def getMinimum(self):
        return self.minimum
    def getMinimumInterval(self):
        d, u = self.leftInf, self.rightInf
        if self.lCount:
            d = -self.l[0]
        if self.rCount:
            u = self.r[0]
        return (d, u)
    def addValue(self, a):
        self.minimum += a
    def addRightLamp(self, a):
        u = self.leftInf
        if self.lCount:
            u = -self.l[0]
        heappush(self.l, -a)
        t = -heappop(self.l)
        heappush(self.r, t)
        self.rCount += 1
        if u > a:
            self.minimum += u - a
    def addLeftLamp(self, a):
        u = self.rightInf
        if self.rCount:
            u = self.r[0]
        heappush(self.r, a)
        t = heappop(self.r)
        heappush(self.l, -t)
        self.lCount += 1
        if a > u:
            self.minimum += a - u
    def addMagnitude(self, a):
        self.addLeftLamp(a)
        self.addRightLamp(a)
