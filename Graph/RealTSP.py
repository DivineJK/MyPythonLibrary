from heapq import heappush, heappop
class real_traveling_salesman_problem:
    def __init__(self, n):
        self.n = n
        self.k = 0
        self.neighbor = {i: [] for i in range(self.n)}
        self.dist = {}
        self.INF = int(1e18)
        self.mind = []
        self.prev = []
        self.routes = []
        self.subdist = []
        self.chkp = []
        self.prev_r = []
    def set_edges(self, x, y, c):
        if x*self.n+y in self.dist:
            self.dist[x*self.n+y] = min(c, self.dist[x*self.n+y])
        else:
            self.neighbor[x].append(y)
            self.dist[x*self.n+y] = c
        if y*self.n+x in self.dist:
            self.dist[y*self.n+x] = min(self.INF, self.dist[y*self.n+x])
        else:
            self.neighbor[y].append(x)
            self.dist[y*self.n+x] = self.INF
    def dijkstra(self, x, inc=True):
        pq = []
        self.chkp.append(x)
        self.subdist.append([0 for _ in range(self.k+1)])
        for i in range(self.k):
            self.subdist[i].append(0)
        for i in range(self.n):
            self.mind.append(self.INF)
            self.prev.append(-1)
        self.mind[self.k*self.n+x] = 0
        for i in range(self.n):
            heappush(pq, [self.mind[self.k*self.n+i], i])
        while pq != []:
            b = heappop(pq)
            r = b[1]
            for i in self.neighbor[r]:
                if self.mind[self.k*self.n+i] > self.mind[self.k*self.n+r] + self.dist[r*self.n+i]:
                    self.mind[self.k*self.n+i] = self.mind[self.k*self.n+r] + self.dist[r*self.n+i]
                    heappush(pq, [self.mind[self.k*self.n+i], i])
                    self.prev[self.k*self.n+i] = r
        for i in range(self.k):
            self.subdist[-1][i] = self.mind[(self.k)*self.n+self.chkp[i]]
            self.subdist[i][-1] = self.mind[i*self.n+self.chkp[self.k]]
            for j in range(1<<self.k):
                self.routes[i].append(-1)
                self.prev_r[i].append(-1)
        self.k += inc
        self.routes.append([-1 for _ in range(1<<self.k)])
        self.prev_r.append([-1 for _ in range(1<<self.k)])
    def tsp_part(self, bit, v):
        if self.routes[v][bit] != -1:
            return self.routes[v][bit]
        if bit == (1 << v):
            self.routes[v][bit] = 0
            return self.routes[v][bit]
        prev_bit = bit & ~(1 << v)
        res = self.INF
        m = -1
        for i in range(self.k):
            if (1 << i) & prev_bit:
                if res > self.tsp_part(prev_bit, i) + self.subdist[i][v]:
                    res = self.tsp_part(prev_bit, i) + self.subdist[i][v]
                    m = i
        self.routes[v][bit] = res
        self.prev_r[v][bit] = m
        return self.routes[v][bit]
    def mini_route(self, i, j):
        # j -> prev[j] -> ... -> i
        X = [self.chkp[j]]
        while self.prev[i*self.n+X[-1]] != -1:
            X.append(self.prev[i*self.n+X[-1]])
        X.reverse()
        return X
    def get_route(self, v):
        L = [v]
        bit = (1 << self.k) - 1
        while self.prev_r[L[-1]][bit] != -1:
            c = L[-1]
            L.append(self.prev_r[L[-1]][bit])
            bit = bit & ~(1<<c)
        if len(L) == self.k:
            for i in range(self.k):
                L[i] = self.chkp[L[i]]
            LL = [L[0]]
            for i in range(self.k-1):
                X = self.mini_route(i, i+1)
                for j in range(1, len(X)):
                    LL.append(X[j])
            return LL
        else:
            raise ValueError("You cannot visit all vertices.")
