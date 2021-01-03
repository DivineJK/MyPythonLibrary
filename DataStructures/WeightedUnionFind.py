class weighted_union_find:
    def __init__(self, n, sum_id=0):
        self.par = [i for i in range(n)]
        self.size = [1]*n
        self.weight = [sum_id]*n
        self.validity = True
    def root(self, x):
        if self.par[x] == x:
            return x
        r = self.root(self.par[x])
        self.weight[x] += self.weight[self.par[x]]
        self.par[x] = r
        return self.par[x]
    def same(self, x, y):
        return self.root(x) == self.root(y)
    def weighten(self, x):
        self.root(x)
        return self.weight[x]
    def unite(self, x, y, w):
        r_x, r_y = self.root(x), self.root(y)
        if r_x == r_y:
            if self.weighten(x) + w != self.weighten(y):
                self.validity = False
        else:
            w += self.weighten(x)
            w -= self.weighten(y)
            if self.size[r_x] < self.size[r_y]:
                r_x, r_y = r_y, r_x
                w = -w
            self.weight[r_y] = w
            self.par[r_y] = r_x
            self.size[r_x] += self.size[r_y]
