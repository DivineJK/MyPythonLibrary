class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.size = [1]*n
        self.groupCount = n
    def root(self, x):
        t = x
        while self.par[t] != t:
            t = self.par[t]
        s = x
        while self.par[s] != t:
            s, self.par[s] = self.par[s], t
        return t
    def getSize(self, x):
        return self.size[self.root(x)]
    def getGroupCount(self):
        return self.groupCount
    def same(self, x, y):
        return self.root(x) == self.root(y)
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x != y:
            self.groupCount -= 1
            if self.size[x] < self.size[y]:
                x, y = y, x
            self.par[y] = x
            self.size[x] += self.size[y]
