from heapq import heappush, heappop
class tsp_solver:
    def __init__(self, n, INF):
        self.n = n
        self.k = 0
        self.INF = INF
        self.graph = [[] for _ in range(n)]
        self.dist_d = {}
        self.cost = []
        self.chkp = []
        self.sub_cost = []
        self.routes = []
        self.prev_r = []
        self.prev = []
    def connect_edge(self, u, v, c=1, directed=True):
        self.graph[u].append(v)
        if u*self.n+v in self.dist_d:
            if self.dist_d[u*self.n+v] > c:
                self.dist_d[u*self.n+v] = c
        else:
            self.dist_d[u*self.n+v] = c
        if not directed:
            self.graph[v].append(u)
            if v*self.n+u in self.dist_d:
                if self.dist_d[v*self.n+u] > c:
                    self.dist_d[v*self.n+u] = c
            else:
                self.dist_d[v*self.n+u] = c
    def add_checkpoint(self, x):
        self.chkp.append(x)
        for i in range(self.n):
            self.cost.append(self.INF)
            self.prev.append(-1)
        for i in range(self.k):
            self.sub_cost[i].append(self.INF)
            for j in range(1<<self.k):
                self.routes[i].append(-1)
                self.prev_r[i].append(-1)
        self.k += 1
        self.sub_cost.append([self.INF]*self.k)
        self.routes.append([-1]*(1<<self.k))
        self.prev_r.append([-1]*(1<<self.k))
    def bfs(self, x):
        p = self.chkp[x]
        st = [p]
        self.cost[x*self.n+p] = 0
        flg = [True]*self.n
        flg[p] = False
        pnt = 0
        cnt = 1
        d = 0
        while pnt < cnt:
            tmp = cnt
            d += 1
            for i in range(pnt, cnt):
                for j in self.graph[st[i]]:
                    if flg[j]:
                        self.cost[x*self.n+j] = d
                        st.append(j)
                        flg[j] = False
                        cnt += 1
                        self.prev[x*self.n+j] = st[i]
            pnt = tmp
        for i in range(self.k):
            self.sub_cost[x][i] = self.cost[x*self.n+self.chkp[i]]
    def dijkstra(self, x):
        p = self.chkp[x]
        self.cost[x*self.n+p] = 0
        pq = []
        for i in range(self.n):
            heappush(pq, (self.cost[x*self.n+i], i))
        while pq != []:
            b = heappop(pq)
            r = b[1]
            for i in self.graph[r]:
                if self.cost[x*self.n+i] > self.cost[x*self.n+r] + self.dist_d[r*self.n+i]:
                    self.cost[x*self.n+i] = self.cost[x*self.n+r] + self.dist_d[r*self.n+i]
                    heappush(pq, (self.cost[x*self.n+i], i))
                    self.prev[x*self.n+i] = r
        for i in range(self.k):
            self.sub_cost[x*self.n+i] = self.cost[x*self.n+self.chkp[i]]
    def tsp_part(self, bit, v):
        if self.routes[v][bit] >= 0:
            return self.routes[v][bit]
        if bit == (1 << v):
            self.routes[v][bit] = 0
            return 0
        res = self.INF
        prev_bit = bit & ~(1 << v)
        p = -1
        for i in range(self.k):
            if (1 << i) & prev_bit:
                tmp = self.tsp_part(prev_bit, i)
                if res > tmp + self.sub_cost[i][v]:
                    res = tmp + self.sub_cost[i][v]
                    p = i
        self.routes[v][bit] = res
        self.prev_r[v][bit] = p
        return self.routes[v][bit]
