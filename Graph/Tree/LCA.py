class LCA:
    def __init__(self, n, counter=[]):
        self.n = n
        self.counter = [0]*n
        self.cumulative_counter = [0]*n
        if len(counter) == n:
            for i in range(n):
                self.counter[i] = counter[i]
        self.bin_top = len(bin(n))-1
        self.graph = [[] for _ in range(n)]
        self.parent = [[-1]*n for _ in range(self.bin_top)]
        self.distD = {}
        self.depth = [0]*n
        self.cost = [0]*n
    def connect_edge(self, x, y, c, undirected=True):
        self.graph[x].append(y)
        if x*self.n+y in self.distD:
            self.distD[x*self.n+y] = min(c, self.distD[x*self.n+y])
        else:
            self.distD[x*self.n+y] = c
        if undirected:
            self.graph[y].append(x)
            if y*self.n+x in self.distD:
                self.distD[y*self.n+x] = min(c, self.distD[y*self.n+x])
            else:
                self.distD[y*self.n+x] = c
    def bfs(self, a):
        p = [a]
        flg = [True]*self.n
        flg[a] = False
        pnt = 0
        cnt = 1
        self.depth[a] = 0
        self.cumulative_counter[a] = self.counter[a]
        d = 0
        while pnt < cnt:
            m = cnt
            d += 1
            for i in range(pnt, cnt):
                c = p[i]
                for j in self.graph[c]:
                    if flg[j]:
                        self.cumulative_counter[j] = self.cumulative_counter[c] + self.counter[j]
                        self.depth[j] = d
                        self.cost[j] = self.cost[c] + self.distD[c*self.n+j]
                        self.parent[0][j] = c
                        p.append(j)
                        flg[j] = False
                        cnt += 1
            pnt = m
        for i in range(1, self.bin_top):
            for j in range(self.n):
                if self.parent[i-1][j] < 0:
                    self.parent[i][j] = -1
                else:
                    self.parent[i][j] = self.parent[i-1][self.parent[i-1][j]]
    def LCA(self, x, y):
        if self.depth[x] > self.depth[y]:
            x, y = y, x
        for i in range(self.bin_top):
            if ((self.depth[y] - self.depth[x]) >> i) & 1:
                y = self.parent[i][y]
        if x == y:
            return x
        for i in range(self.bin_top, 0, -1):
            if self.parent[i-1][x] != self.parent[i-1][y] and self.parent[i-1][x] != -1 and self.parent[i-1][y] != -1:
                x = self.parent[i-1][x]
                y = self.parent[i-1][y]
        return self.parent[0][x]
