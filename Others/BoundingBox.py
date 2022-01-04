class BoundingBox:
    def __init__(self):
        self.position = (0, 0)
        self.size = (0, 0)
        self.isEmpty = True
    def isInner(self, p):
        if self.isEmpty:
            return False
        xi = self.position[0] <= p[0] and p[0] <= self.position[0] + self.size[0]
        yi = self.position[1] <= p[1] and p[1] <= self.position[1] + self.size[1]
        return xi and yi
    def unite(self, p):
        if not self.isInner(p):
            self.isEmpty = False
            x = self.size[0]
            y = self.size[1]
            a = self.position[0]
            b = self.position[1]
            if p[0] < self.position[0]:
                x += self.position[0] - p[0]
                a = p[0]
            if p[1] < self.position[1]:
                y += self.position[0] - p[0]
                b = p[1]
            if p[0] > self.position[0] + self.size[0]:
                x += p[0] - self.position[0]
            if p[1] > self.position[1] + self.size[1]:
                y += p[1] - self.position[1]
            self.position = (a, b)
            self.size = (x, y)
            
def convertStringMapToIntegerMap(gridMap):
    n = len(gridMap)
    res = [[] for _ in range(n)]
    for i in range(n):
        m = len(gridMap[i])
        for j in range(m):
            res[i].append(ord(gridMap[i][j]))
    return res
def getBoundingBoxSub(gridMap, charWhite):
    n, m = len(gridMap), max(len(i) for i in gridMap)
    cnt = 0
    cntW = 0
    for i in range(n):
        if len(gridMap[i]) < m:
            gridMap[i] = [charWhite]*(m-len(gridMap[i]))
        for j in range(m):
            cnt += 1
            if gridMap[i][j] == charWhite:
                cntW += 1
    if cnt == cntW:
        return []
    xu, xd = -1, n+1
    yl, yr = -1, m+1
    flg = True
    while flg:
        xu += 1
        for i in range(m):
            if gridMap[xu][i] == charWhite:
                continue
            flg = False
            break
    flg = True
    while flg:
        xd -= 1
        for i in range(m):
            if gridMap[xd-1][i] == charWhite:
                continue
            flg = False
            break
    flg = True
    while flg:
        yl += 1
        for i in range(xu, xd):
            if gridMap[i][yl] == charWhite:
                continue
            flg = False
            break
    flg = True
    while flg:
        yr -= 1
        for i in range(xu, xd):
            if gridMap[i][yr-1] == charWhite:
                continue
            flg = False
            break
    res = [[0]*(yr-yl) for i in range(xd-xu)]
    for i in range(xu, xd):
        for j in range(yl, yr):
            res[i-xu][j-yl] = gridMap[i][j]
    return res
def getBoundingBox(gridMap, charWhite):
    x = ord(charWhite)
    ngm = convertStringMapToIntegerMap(gridMap)
    return getBoundingBoxSub(ngm, x)
def getBoundingBoxInt(gridMap, charWhite):
    return getBoundingBoxSub(gridMap, charWhite)
