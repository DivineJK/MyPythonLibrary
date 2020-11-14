class union_find:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.size = [1]*n
    def root(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]
    def same(self, x, y):
        return self.root(x) == self.root(y)
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x != y:
            if self.size[x] < self.size[y]:
                x, y = y, x
            self.par[y] = x
            self.size[x] += self.size[y]
