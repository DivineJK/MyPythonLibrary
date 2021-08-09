class AffineSpace2d:
    def reset(self):
        self.originX = 0
        self.originY = 0
        self.baseFirstX = 1
        self.baseFirstY = 0
        self.baseSecondX = 0
        self.baseSecondY = 1
        self.historyOriginX = [0]
        self.historyOriginY = [0]
        self.historyBaseFirstX = [1]
        self.historyBaseFirstY = [0]
        self.historyBaseSecondX = [0]
        self.historyBaseSecondY = [1]
        self.transformTime = 0
    def addHistory(self):
        self.historyOriginX.append(self.originX)
        self.historyOriginY.append(self.originY)
        self.historyBaseFirstX.append(self.baseFirstX)
        self.historyBaseFirstY.append(self.baseFirstY)
        self.historyBaseSecondX.append(self.baseSecondX)
        self.historyBaseSecondY.append(self.baseSecondY)
        self.transformTime += 1
    def __init__(self):
        self.reset()
    def getTransformedPoint(self, x, y, after=-1):
        time = after
        if after == -1:
            time = self.transformTime
        u1, v1 = self.historyBaseFirstX[after], self.historyBaseFirstY[after]
        u2, v2 = self.historyBaseSecondX[after], self.historyBaseSecondY[after]
        x, y = u1 * x + u2 * y, v1 * x + v2 * y
        p, q = self.historyOriginX[after], self.historyOriginY[after]
        x += p
        y += q
        return (x, y)
    def translate(self, x, y):
        self.originX += x
        self.originY += y
        self.addHistory()
    def rotate90CounterClockwise(self):
        self.originX, self.originY = -self.originY, self.originX
        self.baseFirstX, self.baseFirstY = -self.baseFirstY, self.baseFirstX
        self.baseSecondX, self.baseSecondY = -self.baseSecondY, self.baseSecondX
        self.addHistory()
    def rotate90Clockwise(self):
        self.originX, self.originY = self.originY, -self.originX
        self.baseFirstX, self.baseFirstY = self.baseFirstY, -self.baseFirstX
        self.baseSecondX, self.baseSecondY = self.baseSecondY, -self.baseSecondX
        self.addHistory()
    def mirrorX(self, p):
        self.originX = 2*p - self.originX
        self.baseFirstX = -self.baseFirstX
        self.baseSecondX = -self.baseSecondX
        self.addHistory()
    def mirrorY(self, p):
        self.originY = 2*p - self.originY
        self.baseFirstY = -self.baseFirstY
        self.baseSecondY = -self.baseSecondY
        self.addHistory()
