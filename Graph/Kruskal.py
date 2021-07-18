class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.size = [1]*n
    def root(self, x):
        t = x
        while self.par[t] != t:
            t = self.par[t]
        s = x
        while self.par[s] != t:
            s, self.par[s] = self.par[s], t
        return t
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

def Kruskal(n, graph):
    # graph[i] = (c, a, b). it must be guaranteed that graph is sorted.
    uf = UnionFind(n)
    m = len(graph)
    res = []
    for i in range(m):
        if uf.same(graph[i][1], graph[i][2]):
            continue
        cost += graph[i][0]
        uf.unite(graph[i][1], graph[i][2])
        res.append((graph[i][1], graph[i][2], graph[i][0]))
    return res
