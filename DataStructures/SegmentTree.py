class SegmentTree:
    def __init__(self, n, identity, op, upd, initial = []):
        self.size = n
        if self.size & (self.size - 1):
            while self.size & (self.size - 1):
                self.size &= self.size - 1
            self.size <<= 1
        self.identity = identity
        self.binaryOperator = op
        self.updateOperator = upd
        self.tree = [self.identity]*(self.size<<1)
        m = min(self.size, len(initial))
        for i in range(m):
            self.tree[i+self.size] = initial[i]
        for i in range(self.size-1, 0, -1):
            self.tree[i] = self.binaryOperator(self.tree[i<<1], self.tree[(i<<1)|1])
    def changeSize(self, newSize, newArray = []):
        t = newSize
        if t & (t - 1):
            while t & (t - 1):
                t &= t - 1
            t <<= 1
        if t <= self.size:
            m = len(newArray)
            if m > t:
                m = t
            for i in range(m):
                self.tree[i+t] = newArray[i]
            for i in range(m, t):
                self.tree[i+t] = self.identity
            for i in range(t-1, 0, -1):
                self.tree[i] = self.binaryOperator(self.tree[i<<1], self.tree[(i<<1)|1])
            self.size = t
        else:
            self.tree = [self.identity]*t
            m = min(t, len(newArray))
            for i in range(m):
                self.tree[i+t] = newArray[i]
            for i in range(t-1, 0, -1):
                self.tree[i] = self.binaryOperator(self.tree[i<<1], self.tree[(i<<1)|1])
            self.size = t
    def update(self, p, x):
        self.tree[p+self.size] = self.updateOperator(self.tree[p+self.size], x)
        t = (p + self.size) >> 1
        while t:
            u = self.binaryOperator(self.tree[t<<1], self.tree[(t<<1)|1])
            if u == self.tree[t]:
                break
            self.tree[t] = u
            t >>= 1
    def getSegment(self, l, r):
        left, right = l + self.size, r + self.size
        f, s = [], []
        fc, sc = 0, 0
        while left < right:
            if left & 1:
                f.append(left)
                left += 1
                fc += 1
            left >>= 1
            if right & 1:
                s.append(right-1)
                right -= 1
                sc += 1
            right >>= 1
        res = self.identity
        for i in range(fc):
            res = self.binaryOperator(res, self.tree[f[i]])
        for i in range(sc, 0, -1):
            res = self.binaryOperator(res, self.tree[s[i-1]])
        return res
    def bisect(self, val):
        t = 1
        u = self.identity
        while t < self.size:
            t <<= 1
            x = self.binaryOperator(u, self.tree[t])
            if x < val:
                u = x
                t += 1
        return t - self.size
